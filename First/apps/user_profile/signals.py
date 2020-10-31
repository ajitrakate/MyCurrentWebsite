# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from .models import Profile, Board_required, Button_required
# from apps.common.models import Board, Button


# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()





# @receiver(post_save, sender=Board)
# def create_board_required(sender, instance, created, **kwargs):
#     if created:
#         Board_required.objects.create(user=instance.user, name=instance.name, desc=instance.desc, manufacturer_name=instance.manufacturer_name, last_updated=instance.last_updated)

# @receiver(post_save, sender=Board)
# def save_board_required(sender, instance, **kwargs):
#     instance.user.Board_required.save()




# @receiver(post_save, sender=Button)
# def create_button_required(sender, instance, created, **kwargs):
#     if created:
#         Button_required.objects.create(Board=instance.Board, name=instance.name, desc=instance.desc, status=instance.status, pin_no=instance.pin_no, last_updated=instance.last_updated)

# @receiver(post_save, sender=Button)
# def save_button_required(sender, instance, **kwargs):
#     instance.Board.user.Board_required.save()


