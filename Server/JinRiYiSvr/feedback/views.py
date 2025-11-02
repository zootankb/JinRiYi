import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt

from datatool import error_code, data_util
from datatool.enum_protocol_id import *
from datatool.error_code import ERROR_ENUM, VERIFICATION_NO_CODE
from feedback.models import CustomerInfo, VerificationCode, Product, Feedback


# Create your views here.


@require_GET
def index(request):
    return HttpResponse("测试接口，能获取到即表示可正常运行")


@csrf_exempt
@require_POST
def start_feedback(request):
    if request.method == "POST":
        json_data = json.loads(request.body.decode('utf-8'))
        # 获取数据
        proj_id = json_data['proj_id']
        tec_name = json_data['tec_name']
        star_svr_num = json_data['star_svr_num']
        star_tec_num = json_data['star_tec_num']
        star_env_num = json_data['star_env_num']
        content = json_data['content']
        nick_name = json_data['nick_name']
        from_platform = json_data['from_platform']
        gender = json_data['gender']
        language = json_data['language']
        city = json_data['city']
        province = json_data['province']
        country = json_data['country']
        avatar_url = json_data['avatar_url']

        product = Product.objects.get(pk=proj_id)

        user = None
        if CustomerInfo.objects.count() == 0:
            user = CustomerInfo()
            user.nick_name = nick_name
            user.from_platform = from_platform
            user.gender = gender
            user.language = language
            user.city = city
            user.province = province
            user.country = country
            user.avatar_url = avatar_url
            user.save()
        else:
            user = CustomerInfo.objects.get(nick_name=nick_name)

        feedback = Feedback.objects.create()
        feedback.product = product
        feedback.user = user
        feedback.master_name = tec_name
        feedback.service_progress = star_svr_num
        feedback.master_technique = star_tec_num
        feedback.environment = star_env_num
        feedback.content = content
        feedback.save()
        return JsonResponse("1", safe=False, json_dumps_params={'ensure_ascii': False})


# @require_GET
def get_verification_code(request):
    verification_code = data_util.get_random_verification_code()
    if verification_code:
        rep = data_util.get_common_rep_data(CODE_GET_VERIFICATION_CODE, verification_code)
        print(rep)
        return JsonResponse(rep, json_dumps_params={'ensure_ascii': False})
    else:
        rep = data_util.get_common_rep_data(CODE_GET_VERIFICATION_CODE, None, VERIFICATION_NO_CODE)
        return JsonResponse(rep, json_dumps_params={'ensure_ascii': False})


@require_GET
def check_verification_valid(request):
    verification_code = request.GET.get("verification_code")
    if verification_code and VerificationCode.objects.count() > 0:
        obj = VerificationCode.objects.get(code=verification_code)
        valid = 0
        if obj.is_valid:
            valid = 1
        rep = data_util.get_common_rep_data(CODE_CHECK_VERIFICATION_CODE, valid)
        return JsonResponse(rep, json_dumps_params={'ensure_ascii': False})
    else:
        rep = data_util.get_common_rep_data(CODE_CHECK_VERIFICATION_CODE, "没有verification_code参数", VERIFICATION_NO_CODE)
        return JsonResponse(rep, json_dumps_params={'ensure_ascii': False})


@require_GET
def get_all_products(request):
    products = Product.objects.all()
    proj_arr = []
    for product in products:
        proj_arr.append({
            'id': product.id,
            'name': product.name,
        })
    print(proj_arr)
    return JsonResponse(proj_arr, safe=False, json_dumps_params={'ensure_ascii': False})
