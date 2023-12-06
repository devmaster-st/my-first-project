from django.db import models


class Guestbook(models.Model):
    user_first_name = models.CharField(max_length=30, blank=False)  # Имя
    user_last_name = models.CharField(max_length=30, blank=False)  # Фамилия
    email = models.EmailField(max_length=50, blank=False)  # Почта
    feedback_frame = models.CharField(max_length=1000, blank=False)  # Текст обратной связи
    checkbox = models.BooleanField(default=False)  # признак черновика

    def __str__(self):
        return f'Отзыв от {self.user_first_name} {self.user_last_name}'
