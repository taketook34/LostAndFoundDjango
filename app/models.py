from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to="photos/%Y/%m/")
    founder_contact = models.CharField(max_length=60, null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}:{self.name}"


    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class Comment(models.Model):
    # прописывать надо post через pk, потом исправлю что бы было сразу
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.pk}: {self.text} {self.pk}"

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"

class FeedbackMessage(models.Model):
    email = models.EmailField(max_length=255)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

# Create your models here.
