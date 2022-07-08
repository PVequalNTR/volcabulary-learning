import requests as rq
import json
r = rq.post("http://127.0.0.1:8000/api/v1/add_category/", data={
    'name': 'first_category',
    'description': '第一個測試',
    'vol_list': [
        'gggg',
    ]
})
print(r.text)


# Create your tests here.