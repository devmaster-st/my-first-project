# from django.http import HttpResponse
# return HttpResponse (text)

from django.shortcuts import render

MENU = {"Главная": "/", "Мои цели": "/goal", "Контакты": "/about", "Обратная связь": "/feedback"}


def main_page(request):
    title = "SUTD student blog"
    data = {"menu": MENU, "title": title}
    return render(request, "./index.html", context=data)


def goal_page(request):
    title = "Мои цели"
    data = {"menu": MENU, "title": title}
    return render(request, "./goal.html", context=data)


def about_page(request):
    title = "Мои контакты"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)
