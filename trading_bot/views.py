from django.contrib import messages
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from accounts.models import User


@login_required
def start_trading(request):
    messages.success(request, "매매를 시작했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    user = request.user
    user.is_trading = True
    user.save()

    return redirect(redirect_url)


@login_required
def end_trading(request):
    messages.success(request, "매매를 중지했습니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    user = request.user
    user.is_trading = False
    user.save()

    return redirect(redirect_url)


def get_trading_requirements(request, username):
    user = User.objects.all().filter(username=username).first()
    requirements = dict()
    requirements['is_trading'] = user.is_trading
    requirements['username'] = user.username

    return JsonResponse(requirements)


def get_trading_user_list(request):
    user_list = User.objects.all()
    result = list(map(lambda x: {"username": x.username,
                                 "secret": x.secret_key,
                                 "api_key": x.api_key,
                                 "is_trading": x.is_trading}, user_list))

    return JsonResponse(result, safe=False)




# def trading_coroutine():
#     while True:
#         is_progress = (yield)

        # if is_progress:
        #     # go1 = go()
        #     next(go1)
        #     # go1.send("d")


# def go():
#     is_true = (yield)
#     while True:
#         print(is_true)


