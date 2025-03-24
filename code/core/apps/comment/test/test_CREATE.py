from django.test import TestCase
from globals.test_objects import create_video, create_user, create_headers
from django.urls import reverse

class TestCreateComments(TestCase) : 

    def create_comment_endpoint(self, id) : 
        return reverse('create_comment', args=[id])
    

    def setUp(self):
        self.video = create_video()
        self.user = create_user()


    def test_create_not_found_video(self) : 
        req = self.client.post(self.create_comment_endpoint(10), headers=create_headers(self.user))
        self.assertEqual(req.status_code, 404)

    def test_create_empty_body(self) : 
        body = {}
        req = self.client.post(self.create_comment_endpoint(self.video.id), data=body, headers=create_headers(self.user))
        self.assertEqual(req.status_code, 400)

    def test_create_comment_unauthorized(self) :
        body = {
            'content' : 'test'
        }
        req = self.client.post(self.create_comment_endpoint(self.video.id), data=body)
        self.assertEqual(req.status_code, 401)
        

    def test_create_comment_success(self) :
        body = {
            'content' : 'test'
        }
        req = self.client.post(self.create_comment_endpoint(self.video.id), data=body, headers=create_headers(self.user))
        self.assertEqual(req.status_code, 201)
        