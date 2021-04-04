from common import errors
from lib.sms import send_sms,generator_vcode
from lib.http import render_json
from common import keys
from django.core.cache import cache
from user.models import User


def submit_phone(request):
    """
    获取短信验证码
    :param request:
    :return: POST请求失败或成功 成功则发送
    """
    #判断POST请求
    if not request.method == 'POST':
        return render_json('request method error',code=errors.REQUEST_ERROR)
    ##获取手机号码
    phone = request.POST.get('phone')
    #发送短信验证码
    result,msg = send_sms(phone)
    return render_json(msg)
#    return HttpResponse('submit phone')  测试服务器是否生效

def submit_vcode(request):
    """
    通过验证码登录注册（获取手机验证码直接登录注册）
    :param request:
    :return: 成功则创建用户 失败则报错
    """

    # 判断POST请求
    if not request.method == 'POST':
        return render_json('request method error', code=errors.REQUEST_ERROR)
    phone = request.POST.get('phone')
    # 取到发送给手机的验证码（取到手机上的验证码）
    vcode = request.POST.get('vcode')
    #取到缓存当中的验证码
    cache_vcode = cache.get(keys.VCODE_KEY%phone)
    #两个验证码进行对比 是否一致
    if vcode == cache_vcode:
        # user = User.objects.filter(phonenum=phone)
        # if not user:
        #     #如果没有这个用户 则去创建一个用户
        #     User.objects.create(phonenum=phone,nickname=phone)
        user, _ = User.objects.get_or_create(phonenum=phone,nickname=phone)
        request.session['uid'] = user.id
        return render_json(user.to_string())
    else:
        return render_json('verify code error',errors.VCODE_ERROR)

def get_profile(request):
    """获取个人资料"""
    pass


def set_profile(request):
    """修改个人资料"""
    pass


def upload_avtar(request):
    """头像上传"""
    pass



