from django.shortcuts import render
from .models import Guestbook
MENU = {"Главная": "/", "Мои цели": "/goal", "Контакты": "/about", "Обратная связь": "/feedback"}


def feedback_page(request):
    guestbook = Guestbook.objects.all()
    title = "Обратная связь"
    data = {"menu": MENU, "title": title, "guestbook": guestbook}
    return render(request, "./feedback.html", context=data)


def add_comment_page(request):
    guestbook = Guestbook.objects.all()
    title = "Добавить комментарий"
    data = {"menu": MENU, "title": title, "guestbook": guestbook}
    return render(request, "./add_comment.html", context=data)


def thanks_page(request):
    user_first_name = request.POST['user_first_name']
    user_last_name = request.POST['user_last_name']
    email = request.POST['email']
    feedback_frame = request.POST['feedback_frame']
    Guestbook.objects.create(user_first_name=user_first_name, user_last_name=user_last_name,
                             email=email, feedback_frame=feedback_frame,)
    title = "Благодарю за отзыв"
    data = {"menu": MENU, "title": title, "user_first_name": user_first_name, "user_last_name": user_last_name}
    return render(request, "./thanks.html", context=data)


# Create your views here.
