from django.http import HttpResponseRedirect


def check_login(fn):
    def wrapper(request, *args, **kwargs):
        # print(request.COOKIES.get('IS_LOGIN'))

        if request.COOKIES.get('IS_LOGIN', None):
            return fn(request, *args, *kwargs)
        else:
            # 获取用户当前访问的url，并传递给/user/login/
            next = request.get_full_path()
            # print(next)
            red = HttpResponseRedirect('/users/login/?next=' + next)
            return red

    return wrapper
