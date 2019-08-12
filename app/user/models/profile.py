from django.db import models


class Profile(models.Model):
    """Profile model."""

    user = models.OneToOneField('user.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='user/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)

    movies_create = models.PositiveIntegerField(default=0)
    movies_recomment = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user)
