
from time import sleep

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from User.models import Profile
from Article.models import ArticlePost, ArticleColumn
from django.urls import reverse
class ArtitclePostViewTests(TestCase):

    def test_increase_views(self):
        # 请求详情视图时，阅读量 +1
        author = User(username='user4', password='test_password')
        author.save()
        article = ArticlePost(
            author=author,
            title='test4',
            content='test4',
            )
        article.save()
        self.assertIs(article.total_views, 0)

        url = reverse('article_detail', args=(article.id,))
        response = self.client.get(url)

        viewed_article = ArticlePost.objects.get(id=article.id)
        self.assertIs(viewed_article.total_views, 1)

    def test_increase_views_but_not_change_updated_field(self):
        # 请求详情视图时，不改变 updated 字段
        author = User(username='user5', password='test_password')
        author.save()
        article = ArticlePost(
            author=author,
            title='test5',
            content='test5',
            )
        article.save()

        sleep(0.5)

        url = reverse('article_detail', args=(article.id,))
        response = self.client.get(url)

        viewed_article = ArticlePost.objects.get(id=article.id)
        self.assertIs(viewed_article.update_time - viewed_article.create_time < timezone.timedelta(seconds=0.1), True)