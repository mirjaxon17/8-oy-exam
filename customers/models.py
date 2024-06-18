from django.db import models


class TeleUsers(models.Model):
    first_name = models.CharField(verbose_name="Full Name", max_length=100, null=True, blank=False)
    username = models.CharField(verbose_name="Username", max_length=30, unique=True, null=True)
    telegram_id = models.PositiveBigIntegerField(verbose_name="Telegram Id", unique=True)

    def __str__(self):
        return self.username


class UserMadel(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.TextField(null=True)
    is_staff = models.BooleanField(default=False, null=True)
    telegram_id = models.PositiveBigIntegerField(verbose_name="Telegram Id", unique=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username
