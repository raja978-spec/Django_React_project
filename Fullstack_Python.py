#   CREATE VIRTUAL ENVIRONMENT USING PIPENV
'''
Move to your project directory and run this 
following command. Before that we have to install

pipenv using pip3 install pipenv

pipenv shell -> creates virtual environment file
with the name of Pipfile

Pipfile:

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"
djangorestframework = "*"
django-rest-knox = "*"

[dev-packages]

[requires]
python_version = "3.9"


'''

#              CREATING SERIALIZER
'''
* It is a component used to convert complex data 
  types, such as Django model instances or other  
  Python data structures, into JSON or other 
  content types

* Serelizer converts object of model to json

* Deserialize the json into instance of model object.

* Used to validate incoming data

from rest_framework import serializers

this is the module used to inherit serialized 
model

MODEL.py:

from django.db import models

# Create your models here.
class Lead(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    message=models.CharField(max_length=500,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
Create an file called serilaizer.py inside app

SERILAIZER.py:

from rest_framework import serializers
from leads.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lead
        fields="__all__"

'''

#    CREATING DJANGO WEBSITE FRONT END WITH REACT
# REFER HERE G:\VS_CODE\Django_React_project\leadmanager
'''

* Create an app with python manage.py command, inside
  that we have to create scr/components, template/frontend
  static/frontend

* React based operations are goes to scr/components
  folder template/frontend are handles the entry 
  point of our app, that is index.js

* And static/frontend has the complied version of
  js files that will generated when npm run build
  command are in run.

'''


#         CREATING VIEWSET
'''
from leads.models import Lead
from leads.serailzer import LeadSerializer
from rest_framework import permission,viewsets

class LeadViewSet(viewsets.ModelViewSet):
    query_set=Lead.objects.all()
    
     the permission_classes attribute is set to 
     [permission.AllowAny], which means that any 
     user, whether authenticated or not, will be 
     allowed to access the API endpoints 

    permission_classes=[
        permission.AllowAny
    ]
    seializer_class=LeadSerializer
'''

#         PARAMETER FOR PERMISSION CLASSES        
'''

1. AllowAny: This permission class allows unrestricted
access to the API view, meaning any user, 
authenticated or not, can access the endpoint.

2. IsAuthenticated: This permission class requires 
that the user making the request must be 
authenticated. Unauthenticated users will be 
denied access.

3. IsAdminUser: Only users with staff/superuser
/admin privileges will be allowed access.

4. IsAuthenticatedOrReadOnly: Unauthenticated users
   can read the data (e.g., GET requests) but need 
   to be authenticated to perform write operations 
   (e.g., POST, PUT, DELETE).

5. IsAuthenticatedOrTokenHasScope: This allows 
   access if the user is authenticated and their 
   access token contains the required scope.
'''

#   BABEL FILE
'''

To work with the following dependency we have to
create the file called babel 
 
 "@babel/core": "^7.22.9",
  "@babel/preset-env": "^7.22.9",
  "@babel/preset-react": "^7.22.5",
  "babel-loader": "^9.1.3",
  "babel-plugin-transform-class-properties": "^6.24.1",
   
After creating the file we have to type the following
json data

{
"presets":["@babel/preset-env","@babel/preset-react"],
"plugins":["transform-class-properties"]
}
'''