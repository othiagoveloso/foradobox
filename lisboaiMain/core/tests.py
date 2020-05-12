from django.test import TestCase
from lisboaiMain.core.models import Post


class TestModelPost(TestCase):
    def setUp(self):
        Post.objects.create(name="thiago", email="thiago@thiago.com", message="Um teste de mensagem")
        

        