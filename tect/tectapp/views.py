from django.shortcuts import render, get_object_or_404, redirect

def main(request):
    return render(request, 'tectapp/main.html')
