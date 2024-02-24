from django.db import models
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    #author
    photo = models.ImageField(upload_to="photos/%Y/%m/", blank=True)
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
    #author
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.pk}: {self.text} {self.pk}"

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"


# Create your models here.
