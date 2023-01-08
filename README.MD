# Annalise.ai Task
## Backend - Software Engineering Skills Task - API Building : Image Tagging System
#### Author : Md Samiul Alim,  Date: 1/8/2023

This repository contains the backend files for Image Tagging System project.


### To run Image Tagging System backend, run the following commands:

1. `pip3 install -r requirements.txt`
2. To create an environment run this command  `virtualenv --python=python3 venv`, then add the environment variables.
3. `python3 manage.py runserver `

### API's and Authentication

#####Basic Auth 
To access the API , provides the username and password.
```
Username : admin@gmail.com
Password : admin123
```

##### 1. Add tag to the system, API
Add tag API:

`/api/add-tags/`

Payloads:
```
payload={'name': 'KEI'}
```
Response:
```
{
    "id": 1,
    "name": "TAG1"
}
```
##### 2. Upload Image to the system, API
Upload Image API:

`/api/upload-image/`

Payloads:
```
payload={'name': 'Town'}
files=[
  ('image',('40525eacbb30f48858f6c7bd8d6fc9b3.jpg',open('40525eacbb30f48858f6c7bd8d6fc9b3.jpg','rb'),'image/jpeg'))
]

```
Response:

```
{
    "id": 1,
    "name": "city image",
    "image": "http://127.0.0.1:8000/media/images/1fb703a2623f0cedcc674e649d7a500d.jpg",
    "tag": 1
}
```

##### 3. Tag a image, API
Tag a Image:

``
http://127.0.0.1:8000/api/tag-image/2/
``

Payload:
``` 
payload={'tag': '2'}
```
Response:
```
{
    "id": 2,
    "name": "Town",
    "image": "http://127.0.0.1:8000/media/images/40525eacbb30f48858f6c7bd8d6fc9b3.jpg",
    "tag": 2
}
```
##### 4. Search a image by tag, API
Search a image by tag

`/api/search-image-by-tag/<tagname>/`

Payload:
```
payload={}
```
Response:
```
{
    "images": [
        {
            "id": 2,
            "name": "Town",
            "image": "images/40525eacbb30f48858f6c7bd8d6fc9b3.jpg",
            "tag_id": 2
        }
    ],
    "message": "Images found by the tag Tia"
}
```
#### To test the API, run test cases for the app
`python manage.py test`


##### Example: python request to access a API, add tag
```

import requests

url = "http://127.0.0.1:8000/api/add-tags/"

payload={'name': 'KEI'}
files=[

]
headers = {
  'Authorization': 'Basic c2FtaXVsY3NlMTVAZ21haWwuY29tOmFkbWluMTIz'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
```
