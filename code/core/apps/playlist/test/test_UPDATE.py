from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers, create_playlist

class TestUpdatePlaylistEndpoint (APITestCase) : 

    def update_playlist_endpoint(self, id) : 
        return reverse('update_playlist', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_update_unauthorized(self) : 
        req = self.client.put(self.update_playlist_endpoint(10))
        self.assertEqual(req.status_code, 401)

    def test_update_forbidden(self) : 
        playlist = create_playlist()
        req = self.client.put(self.update_playlist_endpoint(playlist.id), headers=self.headers)
        self.assertEqual(req.status_code, 403)

    def test_update_empty_body(self) : 
        ps = create_playlist(self.user)
        req = self.client.put(self.update_playlist_endpoint(ps.id), headers=self.headers)
        self.assertEqual(req.status_code, 400)
    
    def test_update_success(self) :
        data = {
            'title' : 'test update'
        } 
        ps = create_playlist(self.user)
        req = self.client.put(self.update_playlist_endpoint(ps.id), data=data,headers=self.headers)
        self.assertEqual(req.status_code, 200)
        

