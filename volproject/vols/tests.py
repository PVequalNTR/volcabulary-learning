from django.test import TestCase
import requests as rq
import json
r = rq.post("http://127.0.0.1:8000/api/v1/add_category", data={
    'name': 'test3',
    'description': 'test2',
    'vol_list': [
        'happy', 
        'sad', 
    ]
})
print(r.text)


# Create your tests here.