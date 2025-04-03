from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers ,create_video

class TestLikeVideosEndpoint(TestCase) : 

    def setUp(self):
        self.user = create_user()
        self.like_video_endpoint = reverse('like_video')
        self.headers = create_headers(self.user)
        self.video = create_video()

    def test_like_video_unauthenticated(self) : 
        req = self.client.post(self.like_video_endpoint)
        self.assertEqual(req.status_code, 401)

    def test_like_video_not_found(self) : 
        data = {
            'video_id' : 10
        }
        req = self.client.post(self.like_video_endpoint, headers=self.headers, data=data)
        self.assertEqual(req.status_code, 404)
    
    def test_like_video_not_active(self) : 
        data = {
            'video_id' : self.video.id
        }
        req = self.client.post(self.like_video_endpoint, data=data, headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    def test_like_video_success(self) : 
        self.video.is_active = True
        self.video.save()
        data = {
            'video_id' : self.video.id
        }
        req = self.client.post(self.like_video_endpoint, data=data, headers=self.headers)
        self.assertEqual(req.status_code, 201)
        self.assertIn(self.user, self.video.likes_by.all())
    
    def test_like_remove(self) : 
        self.video.is_active = True
        self.video.likes_by.add(self.user)
        self.video.save()
        data = {
            'video_id' : self.video.id
        }
        req = self.client.post(self.like_video_endpoint,data=data, headers=self.headers)
        self.assertEqual(req.status_code, 201)
        self.assertNotIn(self.user, self.video.likes_by.all())

