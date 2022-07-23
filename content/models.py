from django.db import models

# Create your models here.


class Feed(models.Model):
    content = models.TextField()         # 글 내용
    image = models.TextField()           # 피드 이미지
    email = models.TextField(default='')        # 글쓴이
    like_count = models.IntegerField()  # 좋아요 수


class Like(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.TextField(default='')
    is_like = models.BooleanField(default=True)


class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    reply_content = models.TextField()


class Bookmark(models.Model):
    content_id = models.IntegerField(default=0)
    email = models.TextField(default='')
    is_marked = models.BooleanField(default=True)
