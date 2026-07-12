# Esse arquivo contém meros exemplos de teste

from rest_framework.test import APITestCase

#from django.test import TestCase
#from rest_framework.authtoken.models import Token
#from .models import Post, Categoria

# Create your tests here.

#class PostModelTest(TestCase):
#    def test_slug_gerado_automaticamente(self):
#        cat = Categoria.objects.create(nome='Dashboards')
#        post = Post.objects.create(
#            titulo='Painel de Vendas', url='http://x.com',
#            descricao='...', categoria=cat
#        )
#        self.assertEqual(post.slug, 'painel-de-vendas')

class PostAPITest(APITestCase):
    def test_token_valido_retorna_200(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.get('/api/status/')
        self.assertEqual(response.status_code, 200)
