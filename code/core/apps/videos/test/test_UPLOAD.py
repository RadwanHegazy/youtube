from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers, create_hashtag, create_video


class TestUploadVideoEndpoint(TestCase) : 

    def setUp(self):
        self.upload_video_endpoint = reverse('upload_video')
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_upload_video_unauthenticated(self) : 
        req = self.client.post(self.upload_video_endpoint)
        self.assertEqual(req.status_code, 401)
    
    def test_upload_video_no_body(self) : 
        req = self.client.post(self.upload_video_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 400)

    def test_upload_video_success(self) : 
        body = {
            'title' : 'test',
            'description' : 'test',
            'thumbnail' : open('test_material/test.jpg', 'rb'),
            'original_video' : open('test_material/test.mp4', 'rb'),
        }
        req = self.client.post(self.upload_video_endpoint, headers=self.headers, data=body)
        self.assertEqual(req.status_code, 201)
