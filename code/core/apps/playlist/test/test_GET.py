from rest_framework.test import APITestCase
from django.urls import reverse
from globals.test_objects import create_user, create_playlist, create_headers, create_video

class TestGetPlaylistEndpoint (APITestCase) : 

    def get_playlist_by_id(self, id) : 
        return reverse('retrive_playlist_id', args=[id])
    
    def setUp(self):
        self.get_playlist_owner = reverse('retrive_playlist_owner')
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_get_owner_playlist_unauthorized(self) : 
        req = self.client.get(self.get_playlist_owner)
        self.assertEqual(req.status_code, 401)
    
    def test_get_owner_playlist_empty(self) : 
        req = self.client.get(self.get_playlist_owner, headers=self.headers)
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['results'], [])
    
    def test_get_owner_playlist_notempty(self) :
        create_playlist(owner=self.user) 
        req = self.client.get(self.get_playlist_owner, headers=self.headers)
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['results'], [])
    
    def test_get_playlist_notfound(self) : 
        req = self.client.get(self.get_playlist_by_id(10))
        self.assertEqual(req.status_code, 404)
    
    def test_get_playlist_emptyvideos(self) :
        pl = create_playlist() 
        req = self.client.get(self.get_playlist_by_id(pl.id))
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['get_videos_list'], [])


    def test_get_playlist_not_emptyvideos(self) :
        pl = create_playlist() 
        pl.videos.add(
            create_video(pl.owner),
        )
        req = self.client.get(self.get_playlist_by_id(pl.id))
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['get_videos_list'], [])
    
    

    
