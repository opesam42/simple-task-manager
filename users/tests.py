from django.test import TestCase
from .models import CustomUser
# Create your tests here.

data = CustomUser.objects.get(username='motunrayo')
print(f'url = {data.profileImage}')
