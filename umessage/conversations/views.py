from django.shortcuts import render

def message_list(request):
    return render(request, 'conversations/message_list.html')