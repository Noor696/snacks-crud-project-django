from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

# Create your tests here.

class SnackTest(TestCase):

    def test_list_view_status(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_list_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_list.html')


    def setUp(self):

        # 1. I will create a user
        self.user = get_user_model().objects.create_user(
            username = 'julia',
            email= 'julia@gmail.com',
            password= 'julia'
        )

        # 2. I will create a snack

        self.snack = Snack.objects.create(
            name= 'testsalad',
            img_url ='ww.',
            amount=2,
            description='',
            purchaser=self.user
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),'testsalad')

    def test_detail_view(self):
        url = reverse('snack_detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')

    def test_create_view(self):

        data={
            'name': 'testsalad',
            'img_url' :'www',
            'amount':2,
            'description':'any thing',
            'purchaser':self.user.id
        }
        url = reverse('snack_create')
        response = self.client.post(path=url,data=data,follow=True) 

# we can test any 3 lines bellow:

        # self.assertEqual(len(Snack.objects.all()),2)
        # self.assertTemplateUsed(response,'snack_detail.html')
        self.assertRedirects(response,reverse('snack_detail',args=[2]))