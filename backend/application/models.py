from django.db import models


class Map(models.Model):
    image = 0  # mock field


class Block(models.Model):
    map_id = models.ForeignKey(Map, on_delete=models.CASCADE, default=None)
    image = models.ImageField(default=0)


class MapLevel(models.Model):
    level_name = models.CharField(max_length=50, default=None)
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE, default=None)


class User(models.Model):
    name = models.CharField(max_length=50, default=None)  # User name
    email = models.EmailField(max_length=50, default=None)  # Email
    password = models.CharField(max_length=50, default=None)  # Password
    level = models.IntegerField(default=1)  # User level
    map_level_id = models.ForeignKey(MapLevel, on_delete=models.CASCADE, default=None)
    photo = 0  # mock field

    def __str__(self):
        return str(self.name) + str(self.email)


class Task(models.Model):
    score = models.IntegerField(default=0)
    type = models.CharField(max_length=50, default=None)
    description = models.TextField(default=None)
    map_level_id = models.ForeignKey(MapLevel, on_delete=models.CASCADE, default=None)


class Chat(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, default=None)


class Solution(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Theory(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, default=None)
    text = models.TextField(default=None)
    video = models.URLField(default=None)


class TaskType(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE, default=None)
    name_type = models.TextField(default=None)


class ProgramTests(models.Model):
    input = models.TextField(default=None)
    output = models.TextField(default=None)
    type_id = models.ForeignKey(TaskType, on_delete=models.CASCADE, default=None)
