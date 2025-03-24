from django.test import TestCase
from globals.test_objects import create_user, create_headers, create_comment
from django.urls import reverse

class TestDeleteComments(TestCase) : 

    def delete_comment_endpoint(self, id) : 
        return reverse('delete_comment', args=[id])
    

    def setUp(self):
        self.user = create_user()
        self.comment = create_comment(user=self.user)


    def test_delete_not_found_comment(self) : 
        req = self.client.delete(self.delete_comment_endpoint(10), headers=create_headers(self.user))
        self.assertEqual(req.status_code, 404)

    def test_delete_unauthorized(self) : 
        req = self.client.delete(self.delete_comment_endpoint(10))
        self.assertEqual(req.status_code, 401)
    
    def test_delete_not_comment_owner(self) : 
        user2 = create_user()
        req = self.client.delete(self.delete_comment_endpoint(self.comment.id), headers=create_headers(user2))
        self.assertEqual(req.status_code, 404)

    def test_delete_comment_success(self) :
        req = self.client.delete(self.delete_comment_endpoint(self.comment.id), headers=create_headers(self.user))
        self.assertEqual(req.status_code, 204)
        