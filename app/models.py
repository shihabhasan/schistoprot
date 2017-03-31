from django.db import models

class SurfaceLessConservative(models.Model):
    sequence = models.TextField(primary_key=True)
    prediction = models.TextField()
    features = models.TextField()
    access = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return self.sequence


class SecretoryLessConservative(models.Model):
    sequence = models.TextField(primary_key=True)
    prediction = models.TextField()
    features = models.TextField()
    access = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return self.sequence

class SurfaceMoreConservative(models.Model):
    sequence = models.TextField(primary_key=True)
    prediction = models.TextField()
    features = models.TextField()
    access = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return self.sequence


class SecretoryMoreConservative(models.Model):
    sequence = models.TextField(primary_key=True)
    prediction = models.TextField()
    features = models.TextField()
    access = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        return self.sequence
