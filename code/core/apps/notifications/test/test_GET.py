from django.test import TestCase
from globals.test_objects import create_user, create_headers, create_notification
from django.urls import reverse

class TestListNotifications (TestCase) : 

    def setUp(self):
        self.notifications_endpoint = reverse('get_notifications')
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_get_unauthorized(self) : 
        req = self.client.get(self.notifications_endpoint)
        self.assertEqual(req.status_code, 401)
    
    def test_get_notification_empty(self) : 
        req = self.client.get(self.notifications_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['count'], 0)
    
    def test_get_notification_not_empty(self) : 
        create_notification(reciver=self.user)
        req = self.client.get(self.notifications_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['count'], 0)

    def test_get_notification_make_sender(self) : 
        create_notification(sender=self.user)
        req = self.client.get(self.notifications_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['count'], 0)
    
    
