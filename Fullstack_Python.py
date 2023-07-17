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