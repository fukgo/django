from django.db import models
from django.contrib.auth.models import User
from Article.models import ArticlePost
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey
class Comment(MPTTModel):
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    #content = models.TextField(),更换为富文本编辑器
    content = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    # 新增，mptt树形结构
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='replyers')
    """    class Meta:
        ordering = ('created',)"""
    class MPTTMeat:
        order_insertion_by = ['created']

    def __str__(self):
        return self.content[0:20]
