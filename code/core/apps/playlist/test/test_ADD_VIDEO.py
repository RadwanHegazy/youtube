from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers, create_playlist, create_video

class TestAddVideoPlaylistEndpoint (APITestCase) : 

    def addvideo_playlist_endpoint(self, id) : 
        return reverse('add_playlist_video', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_add_unauthorized(self) : 
        req = self.client.post(self.addvideo_playlist_endpoint(10))
        self.assertEqual(req.status_code, 401)

    def test_add_forbidden(self) : 
        ps = create_playlist()
        req = self.client.post(self.addvideo_playlist_endpoint(ps.id), headers=self.headers)
        self.assertEqual(req.status_code, 403)

    def test_add_notfound_playlist(self) :
        req = self.client.post(self.addvideo_playlist_endpoint(999), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    def test_add_no_body(self) :
        ps = create_playlist(self.user)
        req = self.client.post(self.addvideo_playlist_endpoint(ps.id), headers=self.headers)
        self.assertEqual(req.status_code, 400)
    
    
    def test_add_video_notfound(self) :
        data = {
            'video_id' : 999
        }
        ps = create_playlist(self.user)
        req = self.client.post(self.addvideo_playlist_endpoint(ps.id), data=data,headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    
    def test_add_video_not_owner(self) :
        data = {
            'video_id' : create_video().id
        }
        ps = create_playlist(self.user)
        req = self.client.post(self.addvideo_playlist_endpoint(ps.id), data=data,headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    
    def test_add_video_success(self) :
        data = {
            'video_id' : create_video(self.user).id
        }
        ps = create_playlist(self.user)
        req = self.client.post(self.addvideo_playlist_endpoint(ps.id), data=data,headers=self.headers)
        self.assertEqual(req.status_code, 201)
    


    

        
    



    
