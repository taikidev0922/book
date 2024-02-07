from django.db import models

CATEGORY = (
    ('business','ビジネス'),
    ('technology','テクノロジー'),
    ('philosophy','哲学'),)

class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY,
    )

    def __str__(self):
        return self.title