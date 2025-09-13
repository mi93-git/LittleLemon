from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer 

class MenuViewTest(TestCase):
    def setup(self):
        self.client = Client()
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=100, inventory=10)

    def test_getall(self):
        response = self.client.get("/restaurant/menu/")

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, serializer.data)