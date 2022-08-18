from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    
    GENRE = (
        ('HF', 'HISTORICAL FICTION'),
        ('FA', 'FANTASY'),
        ('CHL', 'CHILDREN'),
        ('SCI', 'SCIENCE'),
        ('SCF', 'SCIENCE FICTION'),
    )

    genre = models.CharField(max_length=20, choices=GENRE)