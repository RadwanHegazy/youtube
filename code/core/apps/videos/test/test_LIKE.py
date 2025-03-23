from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers ,create_video

class TestLikeVideosEndpoint(TestCase) : 

    def like_video_endpoint(self, id) : 
        return reverse('like_video', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.headers = create_headers(self.user)
        self.video = create_video()

    def test_like_video_unauthenticated(self) : 
        req = self.client.post(self.like_video_endpoint(10))
        self.assertEqual(req.status_code, 401)

    def test_like_video_not_found(self) : 
        req = self.client.post(self.like_video_endpoint(10), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    def test_like_video_not_active(self) : 
        req = self.client.post(self.like_video_endpoint(self.video.id), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    def test_like_video_success(self) : 
        self.video.is_active = True
        self.video.save()
        req = self.client.post(self.like_video_endpoint(self.video.id), headers=self.headers)
        self.assertEqual(req.status_code, 201)
        self.assertIn(self.user, self.video.likes_by.all())
    
    def test_like_remove(self) : 
        self.video.is_active = True
        self.video.likes_by.add(self.user)
        self.video.save()
        req = self.client.post(self.like_video_endpoint(self.video.id), headers=self.headers)
        self.assertEqual(req.status_code, 201)
        self.assertNotIn(self.user, self.video.likes_by.all())

