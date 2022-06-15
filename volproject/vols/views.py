from xml.etree.ElementInclude import LimitedRecursiveIncludeError
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import categories
import json
from .models import categories, Sentence
from .serializers import latest_categoriesSerializer, SentenceSerializer, get_categorySerializer
from django.contrib.auth.models import User, auth
import random
import json
from .Crawler import Cambridge
class latest_categories(APIView):
    def get(self, request, pk, format=None):
        number = categories.objects.all().count()
        if number < (pk - 1) * 10 + 1:
            raise Http404
        elif number < pk * 10:
            category = categories.objects.all()[(pk - 1) * 10 :]
        else :
            category = categories.objects.all()[(pk - 1) * 10 : pk * 10]
        serializer = latest_categoriesSerializer(category, many=True)
        return Response(serializer.data)

class get_category(APIView):
    def get(self, request, name, format=None):
        if categories.objects.filter(name=name).exists():
            category = categories.objects.filter(name=name)[0]
            serializer = get_categorySerializer(category)
            return Response(serializer.data)
        else:
            return Response({
                'info': 'category does not exist !'
            }, status=status.HTTP_400_BAD_REQUEST)

def get_by_string(string):
    Category = categories.objects.filter(name = string)[0]
    words = Category.vol_list
    ret = []
    for word in words:
        sentences = list(Sentence.objects.filter(word = word))
        sentence = random.choice(sentences)
        sentence.name = sentence.name.replace(word, f'{word[0]}___{word[(len(word) - 2):]}')
        ret.append(sentence)
    random.shuffle(ret)
    return ret
 
class get_sentences(APIView):
    def get(self, request, string, format=None):
        sentences = get_by_string(string)
        serializer = SentenceSerializer(sentences, many=True)
        return Response(serializer.data)

class check(APIView):
    def post(self, request, name, format=None):
        data = request.data
        count = 0
        for item in data:
            word = Sentence.objects.filter(id = item['id'])[0].word
            if word == item['word']:
                count += 1
        return Response(json.dumps({"score": count}))

class register(APIView):
    def post(self, request, format=None):
        data = request.data
        username = data['username']
        email = data['email']
        password = data['password']
        _password = data['password']
        if password == _password:
            if User.objects.filter(email=email).exists():
                return Response({
                    'info': 'Email already exists !'
                }, status=status.HTTP_400_BAD_REQUEST)
            elif User.objects.filter(username=username).exists():
                return Response({
                    'info': 'Username already exists !'
                }, status=status.HTTP_400_BAD_REQUEST)
            else :
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return Response({
                    'info': 'Success !'
                })

class add_category(APIView):
    def post(self, request, format=None):
        data = request.data
        name = data['name']
        description = data['description']
        vol_list = dict(request.data)['vol_list']
        if categories.objects.filter(name = name).exists():
            return Response({
                'info': 'Category\'s name had been used !'
            }, status=status.HTTP_400_BAD_REQUEST)
        else :
            new_category = categories.objects.create(name = name, description = description, vol_list = vol_list)
            new_category.save()
            buildwords(vol_list)
            return Response({
                'info': 'Success !'
            })

def buildwords(vol_list):
    for word in vol_list:
        if Sentence.objects.filter(word = word).exists():
            continue
        else:
            listEn, listCh = Cambridge.GetWebData(word)
            for i in range(len(listEn)):
                sentence = listEn[i]
                if len(sentence) > 100:
                    continue
                Sentence.objects.create(name = sentence, word = word, source = 'Cambridge')