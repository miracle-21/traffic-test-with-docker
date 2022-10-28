import json
from django.test import TestCase, Client
from datetime import datetime

from users.models     import User


class UserTest(TestCase):
    # def setUp(self):
    #     User.objects.create(
    #         id= 1,
    #         name= 'minha'
    #     )

    # def tearDown(self):
    #     User.objects.all().delete
    
    def test_user_post(self):
        client= Client()
        user = {
            'name' : 'minha'
        }
        response= client.post('/users', json.dumps(user), content_type='application/json')

        self.assertEqual(response.json(),
        {
            "result": [
                {
                    "name": "minha",
                    "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "ip": '127.0.0.1'
                }
            ]
        })
        self.assertEqual(response.status_code, 200)