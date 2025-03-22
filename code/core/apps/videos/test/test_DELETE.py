from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers, create_video


class TestDeleteVideosEndpoint(TestCase) : 

    def delete_video_endpoint(self, id) : 
        return reverse('delete_video', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_delete_unauthorized(self) : 
        req = self.client.delete(self.delete_video_endpoint(10))
        self.assertEqual(req.status_code, 401)
    
    def test_delete_not_video_owner(self) : 
        video = create_video()
        req = self.client.delete(self.delete_video_endpoint(video.id), headers=self.headers)
        self.assertNotEqual(req.status_code, 200)

    def test_delete_video_not_active(self) : 
        video = create_video(owner=self.user)
        req = self.client.delete(self.delete_video_endpoint(video.id), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    def test_delete_video_not_found(self) : 
        req = self.client.delete(self.delete_video_endpoint(999), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
        
    def test_delete_video_success(self) : 
        video = create_video(owner=self.user, is_active=True)
        req = self.client.delete(self.delete_video_endpoint(video.id), headers=self.headers)
        self.assertEqual(req.status_code, 204)
        
