
from django.test import TestCase

import datetime
from django.utils import timezone
from Article.models import ArticlePost
from django.contrib.auth.models import User
class ArticlePostModelTests(TestCase):

    def test_was_created_recently_with_future_article(self):
        # 若文章创建时间为未来，返回 False
        author = User(username='user', password='test_password')
        author.save()

        future_article = ArticlePost(
            author=author,
            title='test',
            content='test',
            create_time=timezone.now() + datetime.timedelta(days=30)
            )

        self.assertIs(future_article.was_created_recently(), False)
# Create your tests here.
