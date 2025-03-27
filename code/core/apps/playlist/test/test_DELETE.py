from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers, create_playlist

class TestDeletePlaylistEndpoint (APITestCase) : 

    def delete_playlist_endpoint(self, id) : 
        return reverse('delete_playlist', args=[id])
    
    def setUp(self):
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_delete_unauthorized(self) : 
        req = self.client.delete(self.delete_playlist_endpoint(10))
        self.assertEqual(req.status_code, 401)

    def test_delete_forbidden(self) : 
        playlist = create_playlist()
        req = self.client.delete(self.delete_playlist_endpoint(playlist.id), headers=self.headers)
        self.assertEqual(req.status_code, 403)

    def test_delete_notfound(self) : 
        req = self.client.delete(self.delete_playlist_endpoint(999), headers=self.headers)
        self.assertEqual(req.status_code, 404)
    
    def test_delete_success(self) :
        ps = create_playlist(self.user)
        req = self.client.delete(self.delete_playlist_endpoint(ps.id), headers=self.headers)
        self.assertEqual(req.status_code, 204)
