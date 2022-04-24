from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'generator_templates/home.html')


def about(request):
    return render(request, 'generator_templates/about.html')


def password(request):
    selected_password = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')
    upper_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_characters = list("!#$%&*+,-./:;<=>?@^_~")
    numbers = list("1234567890")

    result = list()

    result += characters
    if request.GET.get('uppercase'):
        result += upper_characters
    if request.GET.get('numbers'):
        result += numbers
    if request.GET.get('special'):
        result += special_characters

    length = int(request.GET.get('length', 12))
    for i in range(length):
        selected_password += random.choice(result)
    context = {
        'password': selected_password,
        'result': characters
    }
    return render(request, 'generator_templates/password.html', context)
