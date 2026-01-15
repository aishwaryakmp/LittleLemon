from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=20, inventory=50)
    def test_getall(self):
        #Retrieve all objects
        response = self.client.get('/restaurant/menu/')
        
        #Check if the request was successful
        self.assertEqual(response.status_code, 200)
        
        # We expect 2 items in the JSON response
        self.assertEqual(len(response.data), 2)