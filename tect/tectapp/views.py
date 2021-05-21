from django.shortcuts import render, get_object_or_404, redirect


def main(request):
    return render(request, 'tectapp/index.html')

def recommend(request):
    return redirect('index')
