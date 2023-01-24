from django.test import TestCase
from .models import Autor,Advertise,PayAmount
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from django.test import Client


class AdvertiseTestCase(TestCase):
    def setUp(self):
        c = Client()
        self.response = c.put('/update')
        factory = APIRequestFactory()
        self.request = factory.put('/update')
        

    def create_data(self):
        autor = Autor.objects.filter(is_admin=False).first()
        payment_sum = PayAmount.objects.create(sum=50)
        advertise_1 = Advertise.objects.create(title="first",autor=autor)
        advertise_2 = Advertise.objects.create(title="second",autor=autor)
        advertise_3 = Advertise.objects.create(title="third",autor=autor)

    def create_user(self,username="test"):
        self.user = User.objects.create_user(username=username, password='12345')
        login = self.client.login(username=username, password='12345')
        

    def create_admin_author(self):
        self.create_user("test1")
        admin_author = Autor.objects.create(is_admin=True,user=self.user)
        
    def create_author(self):
        self.create_user()
        admin_author = Autor.objects.create(user=self.user)

    def test_success_update(self):
        self.create_author()
        self.create_admin_author()
        self.create_data()
        response = self.client.put('/update',data={"list": "1,2,3", "status": "оплачено"},content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_with_author(self):
        self.create_author()
        self.create_data()
        response = self.client.put('/update',data={"list": "1,2,3", "status": "оплачено"},content_type='application/json')
        self.assertEqual(response.status_code, 406)

    def test_repeat_update(self):
        self.create_author()
        self.create_admin_author()
        self.create_data()
        self.client.put('/update',data={"list": "1,2,3", "status": "оплачено"},content_type='application/json')
        response = self.client.put('/update',data={"list": "1,2,3", "status": "оплачено"},content_type='application/json')
        print(response.json())
        self.assertEqual(response.status_code, 406)

