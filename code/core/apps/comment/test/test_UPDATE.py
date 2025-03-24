from django.test import TestCase
from globals.test_objects import create_user, create_headers, create_comment
from django.urls import reverse
from rest_framework.test import APIClient


class TestUpdateComments(TestCase) : 

    def update_comment_endpoint(self, id) : 
        return reverse('update_comment', args=[id])
    

    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.comment = create_comment(user=self.user)


    def test_update_not_found_comment(self) : 
        body = {
            'content' : 'new content'
        }
        req = self.client.put(self.update_comment_endpoint(999), headers=create_headers(self.user), data=body)
        self.assertEqual(req.status_code, 404)

    def test_update_unauthorized(self) : 
        req = self.client.put(self.update_comment_endpoint(999))
        self.assertEqual(req.status_code, 401)
    
    def test_update_not_comment_owner(self) : 
        user2 = create_user()
        body = {}
        req = self.client.put(self.update_comment_endpoint(self.comment.id), headers=create_headers(user2), data=body)
        self.assertEqual(req.status_code, 404)

    def test_update_comment_no_body(self) :
        body = {}
        req = self.client.put(self.update_comment_endpoint(self.comment.id), headers=create_headers(self.user), data=body)
        self.assertEqual(req.status_code, 400)
    
    def test_update_comment_success(self) :
        body = {
            'content' : 'new content'
        }
        req = self.client.put(self.update_comment_endpoint(self.comment.id), headers=create_headers(self.user), data=body)
        self.assertEqual(req.status_code, 200)