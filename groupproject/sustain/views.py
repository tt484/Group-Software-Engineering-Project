"""
Module contains the view for the sustainability page
"""
from django.shortcuts import render, redirect
from django.contrib import messages


def sustain(request):
    """Function that retrieves sustain.html if user is logged in"""
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../login')
    return render(request, 'sustain.html')
