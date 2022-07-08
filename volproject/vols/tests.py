import requests as rq
import json
r = rq.post("http://127.0.0.1:8000/api/v1/edit_category/43", data={
    'name': 'first_category',
    'description': '第444個測試',
    'vol_list': [
        'cry',
    ]
})
print(r.text)


# Create your tests here.