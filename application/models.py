from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)  # User name
    email = models.EmailField(max_length=50)  # Email
    password = models.CharField(max_length=50)  # Password
    level = models.IntegerField(default=1)  # User level
    map_id = models.IntegerField(default=0)  # Level of the map (add foreign key to MapLevel PK)
    # photo = models.ImageField()  # User photo

    def __str__(self):
        return self.name + ' ' + self.email


class MapLevel(models.Model):
    level_name = models.CharField()
    block_id = models.TextField()  # (add foreign key to Block PK)


class Block(models.Model):
    map_id = models.IntegerField()  # (add foreign key to Map PK)
    # image = models.ImageField()  # Block picture


class Map(models.Model):
    something = 0  # mock var
    # image = models.ImageField()  # Map picture


# Need to be fixed
class Task(models.Model):
    something = 0  # mock var


class Chat(models.Model):
    task_id = models.IntegerField()  # (add foreign key to Task PK)


class Solution(models.Model):
    task_id = models.IntegerField()  # (add foreign key to Task PK)
    user_id = models.IntegerField()  # (add foreign key to User PK)


class Theory(models.Model):
    task_id = models.IntegerField()  # (add foreign key to Task PK)
    text = models.TextField()
    video = models.URLField()


class TaskType(models.Model):
    task_id = models.IntegerField()  # (add foreign key to Task PK)
    name_type = models.TextField()


class ProgramTests(models.Model):
    input = models.TextField()
    output = models.TextField()
    type_id = models.IntegerField()  # (add foreign key to TaskType PK)
