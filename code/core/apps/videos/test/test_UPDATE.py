from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers, create_video
from rest_framework.test import APIClient


class TestUpdateVideosEndpoint(TestCase) : 

    def update_video_endpoint(self, id) : 
        return reverse('update_video', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.headers = create_headers(self.user)

    def test_update_unauthorized(self) : 
        req = self.client.put(self.update_video_endpoint(10))
        self.assertEqual(req.status_code, 401)
    
    def test_update_not_video_owner(self) : 
        video = create_video()
        req = self.client.put(self.update_video_endpoint(video.id), headers=self.headers)
        self.assertNotEqual(req.status_code, 200)

    def test_update_video_not_active(self) : 
        video = create_video(owner=self.user)
        req = self.client.put(self.update_video_endpoint(video.id), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    def test_update_video_not_found(self) : 
        req = self.client.put(self.update_video_endpoint(999), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
        
    def test_update_video_no_data(self) : 
        video = create_video(owner=self.user, is_active=True)
        req = self.client.put(self.update_video_endpoint(video.id), headers=self.headers)
        self.assertEqual(req.status_code, 400)
        
    def test_update_video_success(self) : 
        video = create_video(owner=self.user, is_active=True)
        data = {
            'title' : 'new_title',
            'description' : 'new_description',
            'thumbnail' : open('test_material/test.jpg', 'rb'),
            'original_video' : open('test_material/test.mp4', 'rb'),
        }
        
        req = self.client.put(self.update_video_endpoint(video.id), headers=self.headers, data=data)
        self.assertEqual(req.status_code, 200)
        
        
