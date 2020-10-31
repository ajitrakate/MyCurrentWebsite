from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_delete
from apps.common.models import Board, Button

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField("Enter somthing about you", max_length=500,blank=True)
    mobile_no = models.CharField("Enter your mobile number", max_length=100, blank=True)

    def __str__(self):
        return f'{self.user}'



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        b = Profile(user=instance)
        b.save()

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

    

class Board_required(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    board_required_identity = models.CharField(max_length=100, default="Change it")
    desc = models.CharField(max_length=200)
    manufacturer_name = models.CharField(max_length=100)
    last_updated = models.DateTimeField()


    def __str__(self):
        return f'{self.user.username}, {self.name}'


@receiver(post_save, sender=Board)
def create_board_required(sender, instance, created, **kwargs):
    if created:
        b = Board_required(user=instance.user, name=instance.name, desc=instance.desc, manufacturer_name=instance.manufacturer_name, last_updated=instance.last_updated, board_required_identity=instance.board_identity)
        b.save()


# @receiver(post_delete, sender=Board)
# def delete_board_required(sender, instance, **kwargs):
#     user = instance.user
#     print(user)
#     identity = instance.identity
#     board = Board_required.objects.filter(identity=identity)[0]
#     print(board)
#     board.delete()

#pre_delete.connect(delete_board_required, sender=Board)




# @receiver(post_save, sender=Board)
# def save_board_required(sender, instance, **kwargs):
#     instance.user.board_required_set.save()






class Button_required(models.Model):
    Board = models.ForeignKey(Board_required, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    button_required_identity = models.CharField(max_length=100, default="Change it")
    desc = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    pin_no = models.IntegerField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return f'{self.Board.user.username}, {self.Board.name}, {self.name}'


@receiver(post_save, sender=Button)
def create_button_required(sender, instance, created, **kwargs):
    if created:
        user = instance.Board.user
        identity_board = instance.Board.identity
        board = Board_required.objects.filter(user=user, identity=identity_board)[0]
        b = Button_required(Board=board, name=instance.name, desc=instance.desc, status=instance.status, pin_no=instance.pin_no, last_updated=instance.last_updated, button_required_identity=instance.button_identity)
        b.save()


# @receiver(post_delete, sender=Button)
# def delete_board_required(sender, instance, **kwargs):
#     user = instance.Board.user
#     board = instance.Board
#     identity = instance.identity
#     button = Button_required.objects.filter(user=user, Board=board, identity=identity)[0]
#     button.delete()



# @receiver(post_save, sender=Button)
# def save_button_required(sender, instance, **kwargs):
#     instance.Board.user.Board_required.save()

    