from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    board_identity = models.CharField(max_length=100, default="Change it")
    desc = models.CharField(max_length=200)
    manufacturer_name = models.CharField(max_length=100)
    last_updated = models.DateTimeField()


    def __str__(self):
        return f'{self.user.username}, {self.name}'
        

    


class Button(models.Model):
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    button_identity = models.CharField(max_length=100, default="Change it")
    desc = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    pin_no = models.IntegerField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return f'{self.Board.user.username}, {self.Board.name}, {self.name}'