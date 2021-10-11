from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import SignupForm
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import login as auth_login

login = LoginView.as_view(template_name="accounts/login_form.html")


def logout(request):
    messages.success(request, '로그아웃되었습니다.')
    return logout_then_login(request)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 성공")
            next_url = request.GET.get('next', '/')
            return redirect(next_url)

    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })

