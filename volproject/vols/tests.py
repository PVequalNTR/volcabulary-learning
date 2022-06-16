from django.test import TestCase
import requests as rq
import json
r = rq.post("http://127.0.0.1:8000/api/v1/add_category", data={
    'name': 'second_category',
    'description': '第一個測試',
    'vol_list': [
        'spring',
        'sad',
        'happy', 
    ]
})
print(r.text)


# Create your tests here.