from django.test import TestCase
from django.conf import settings

# Create your tests here.
customUser = settings.AUTH_USER_MODEL
print(customUser)
print('hello')

def functionsm(name):
    return 'hello {0}'.format(name)

print(functionsm('world'))