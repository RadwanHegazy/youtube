from django.test import TestCase
from globals.test_objects import create_user, create_headers, create_notification
from django.urls import reverse

class TestDeleteNotifications (TestCase) : 

    def delete_notifications_endpoint (self, id):
        return reverse('delete_notifications', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_delete_unauthorized(self) : 
        req = self.client.delete(self.delete_notifications_endpoint(10))
        self.assertEqual(req.status_code, 401)
    
    def test_delete_notification_forbidden(self) :
        notify = create_notification() 
        req = self.client.delete(self.delete_notifications_endpoint(notify.id), headers=self.headers)
        self.assertEqual(req.status_code, 403)
    
    def test_delete_success(self) : 
        notify = create_notification(reciver=self.user) 
        req = self.client.delete(self.delete_notifications_endpoint(notify.id), headers=self.headers)
        self.assertEqual(req.status_code, 204)
