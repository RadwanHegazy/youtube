from django.test import TestCase
from globals.test_objects import create_video, create_comment
from django.urls import reverse

class TestGetComments(TestCase) : 

    def retrive_comment_by_id(self, id) : 
        return reverse('get_comments', args=[id])
    

    def setUp(self):
        self.video = create_video()

    def test_get_not_found_video(self) : 
        req = self.client.get(self.retrive_comment_by_id(10))
        self.assertEqual(req.status_code, 404)

    def test_get_empty_comments(self) : 
        req = self.client.get(self.retrive_comment_by_id(self.video.id))
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['results'], [])

    def test_get_non_empty_comments(self) :
        create_comment(video=self.video) 
        req = self.client.get(self.retrive_comment_by_id(self.video.id))
        self.assertEqual(req.status_code, 200)
        self.assertNotEqual(req.json()['results'], [])