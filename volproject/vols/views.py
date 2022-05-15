from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Latest_categories, Sentence
from .serializers import latest_categoriesSerializer, SentenceSerializer

class latest_categories(APIView):
    def get(self, request, pk, format=None):
        number = Latest_categories.objects.all().count()
        if number < (pk - 1) * 10 + 1:
            raise Http404
        elif number < pk * 10:
            category = Latest_categories.objects.all()[(pk - 1) * 10 :]
        else :
            category = Latest_categories.objects.all()[(pk - 1) * 10 : pk * 10]
        serializer = latest_categoriesSerializer(category, many=True)
        return Response(serializer.data)

class sentence(APIView):
    def get(self, request, s, format=None):
        sentences = Sentence.objects.filter(word = s)
        serializer = SentenceSerializer(sentences, many=True)
        return Response(serializer.data)
