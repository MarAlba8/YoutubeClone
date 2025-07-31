from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase

# Create your tests here.
from django.test import TestCase
from videos.models import Video
from histories.models import History
from histories.views import HistoryListView


class HistoryTestCase(TestCase):
     def setUp(self):
          self.factory = RequestFactory()

          self.user1 = User.objects.create(username="loren", password="test", email="loren@g.com")
          self.user2 = User.objects.create(username="lop", password="test", email="lop@g.com")

          video1 = Video.objects.create(title="title_test1", embed_url="test_url_1", user=self.user1)
          video2 = Video.objects.create(title="title_test2", embed_url="test_url_1", user=self.user2)

          History.objects.create(user=self.user1, video=video1)
          History.objects.create(user=self.user1, video=video2) #Last seen by the user 1
          History.objects.create(user=self.user2, video=video1)

     def test_get_queryset_for_authenticated_user(self):
          request = self.factory.get('/history')

          request.user = self.user1
          view = HistoryListView()
          view.setup(request)
          queryset = view.get_queryset()
          self.assertEqual(queryset.count(), 2)
          self.assertEqual(queryset.first().video.title, 'title_test2')
