from board.models import notice_list
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'board/index.html')

def board_list(request):
    notice = notice_list.objects.all().order_by('-id')
    context = {'notice':notice}
    return render(request, 'board/board_list.html', context)