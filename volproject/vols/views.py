from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import categories, Sentence
from .serializers import latest_categoriesSerializer, SentenceSerializer, get_categorySerializer

import random

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
        category = categories.objects.filter(name=name)[0]
        serializer = get_categorySerializer(category)
        return Response(serializer.data)

def get_by_id(id):
    Category = categories.objects.filter(id = id)[0]
    words = Category.vol_list
    ret = []
    for word in words:
        sentences = list(Sentence.objects.filter(word = word))
        sentence = random.choice(sentences)
        sentence.name = sentence.name.replace(word, f'{word[0]}___{word[(len(word) - 2):]}')
        ret.append(sentence)
    return ret
            
class get_sentences(APIView):
    def get(self, request, id, format=None):
        sentences = get_by_id(id)
        serializer = SentenceSerializer(sentences, many=True)
        return Response(serializer.data)
