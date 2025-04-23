from django.shortcuts import render

def message_list(request):
    return render(request, 'projection/message_list.html')