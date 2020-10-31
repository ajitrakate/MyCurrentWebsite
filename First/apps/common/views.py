from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from apps.common.models import Board, Button
from apps.user_profile.models import Board_required, Button_required
from django.utils import timezone
from django.contrib import messages
import json

# Create your views here.
def home(request):
    return render(request, 'common/home.html')

@login_required
def dashboard(request):
    user = request.user
    boards = user.board_set.all()
    context = {'boards': boards}
    return render(request, 'user_profile/dashboard.html', context)

def buttons(request, board_identity):
    board = Board.objects.filter(board_identity=board_identity)[0]
    buttons = board.button_set.all()
    context = {'buttons': buttons, 'board': board}
    return render(request, 'user_profile/buttons.html', context)

def change_status(request, board_identity, button_identity):
    required_status = request.POST[f'{button_identity}'] 
    board = Board_required.objects.filter(board_required_identity=board_identity)[0]
    button = board.button_required_set.filter(button_required_identity=button_identity)[0]
    current_board = Board.objects.filter(board_identity=board_identity)[0]
    current_button = current_board.button_set.filter(button_identity=button_identity)[0]
    current_button_status = current_button.status
    print(required_status)
    button.status = required_status
    button.last_updated = timezone.now()
    button.save()
    messages.success(request, f'Your request for changing status of {board.manufacturer_name}-{button.name} from {current_button_status} to {required_status}.')
    return redirect('dashboard')

def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'user_profile/profile.html', context)


def post_data(request, board_identity):
    if request.method == "POST":
        board = Board.objects.filter(board_identity=board_identity)[0]
        buttons = board.button_set.all()
        for button in buttons:
            uploaded_status = request.POST[f'{button.button_identity}']
            button.status = uploaded_status
            button.last_updated = timezone.now()
            button.save()
        board_required = Board_required.objects.filter(board_required_identity=board_identity)[0]
        buttons_required = board_required.button_required_set.all()
        print(buttons_required)
        context = {}
        for button in buttons_required:
            context[f'{button.name}'] = button.status
        required_data = json.dumps(context)     
        return HttpResponse(required_data, content_type="text/plain")      
        
    board = Board.objects.filter(board_identity=board_identity)[0]
    buttons = board.button_set.all()
    switches = len(buttons)
    context = {"buttons": buttons, "board": board, "switches": switches}
    return render(request, 'common/post_data.html', context)


class SignUpView(CreateView):
    template_name = 'common/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')





