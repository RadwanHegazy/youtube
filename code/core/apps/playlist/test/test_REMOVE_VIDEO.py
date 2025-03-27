from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers, create_playlist, create_video

class TestRemoveVideoPlaylistEndpoint (APITestCase) : 

    def remove_video_playlist_endpoint(self, id) : 
        return reverse('remove_playlist_video', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_remove_unauthorized(self) : 
        req = self.client.post(self.remove_video_playlist_endpoint(10))
        self.assertEqual(req.status_code, 401)

    def test_remove_forbidden(self) : 
        ps = create_playlist()
        req = self.client.post(self.remove_video_playlist_endpoint(ps.id), headers=self.headers)
        self.assertEqual(req.status_code, 403)

    def test_remove_notfound_playlist(self) :
        req = self.client.post(self.remove_video_playlist_endpoint(999), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    def test_remove_no_body(self) :
        ps = create_playlist(self.user)
        req = self.client.post(self.remove_video_playlist_endpoint(ps.id), headers=self.headers)
        self.assertEqual(req.status_code, 400)
    
    
    def test_remove_video_notfound(self) :
        data = {
            'video_id' : 999
        }
        ps = create_playlist(self.user)
        req = self.client.post(self.remove_video_playlist_endpoint(ps.id), data=data,headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    
    def test_remove_video_not_owner(self) :
        data = {
            'video_id' : create_video().id
        }
        ps = create_playlist(self.user)
        req = self.client.post(self.remove_video_playlist_endpoint(ps.id), data=data,headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    
    def test_remove_video_success(self) :
        video = create_video(self.user)
        
        data = {
            'video_id' : video.id
        }
        ps = create_playlist(self.user)
        ps.videos.add(video)
        req = self.client.post(self.remove_video_playlist_endpoint(ps.id), data=data,headers=self.headers)
        self.assertEqual(req.status_code, 201)
