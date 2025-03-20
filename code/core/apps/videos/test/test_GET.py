from django.test import TestCase
from django.urls import reverse
from globals.test_objects import create_user, create_headers, create_hashtag, create_video


class TestGetVideosEndpoint(TestCase) : 

    def retrive_video_endpoint(self, id) : 
        return reverse('retrive_video', args=[id])
    
    def setUp(self):
        self.list_videos_endpoint = reverse('list_video')
        self.user = create_user()
        self.headers = create_headers(self.user)

    def test_get_list_videoes_anonymous(self) : 
        req = self.client.get(self.list_videos_endpoint)
        self.assertEqual(req.status_code, 200)

    def test_get_list_videos_authenticated_empty(self) : 
        req = self.client.get(self.list_videos_endpoint, headers=self.headers)
        self.assertEqual(req.status_code, 200)

    def test_get_list_videos_authenticated_non_empty(self) : 
        hashtag = create_hashtag()
        create_video(is_active=True, hashtags=[hashtag])
        self.user.hashtags.add(hashtag)
        self.user.save()
        req = self.client.get(self.list_videos_endpoint, headers=self.headers)
        self.assertEqual(req.json()['count'], 1)
        self.assertEqual(req.status_code, 200)

    def test_retrive_not_found_video(self):
        req = self.client.get(self.retrive_video_endpoint(99))
        self.assertEqual(req.status_code, 404)
    
    def test_retrive_video_not_active(self) : 
        vid = create_video(is_active=False)
        req = self.client.get(self.retrive_video_endpoint(vid.id))
        self.assertEqual(req.status_code, 404)
    
    def test_retrive_video_is_active(self) : 
        vid = create_video(is_active=True)
        req = self.client.get(self.retrive_video_endpoint(vid.id))
        self.assertEqual(req.status_code, 200)
    
