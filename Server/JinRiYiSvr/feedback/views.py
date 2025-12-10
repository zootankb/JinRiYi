import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt

from datatool import error_code, data_util
from datatool.enum_data import PlatformChoice, ProductSubType
from datatool.enum_protocol_id import *
from datatool.error_code import ERROR_ENUM, VERIFICATION_NO_CODE
from feedback.models import CustomerInfo, VerificationCode, Product, Feedback, HotProductInfo, ListedInfo
import socket
from JinRiYiSvr.settings import DEBUG

from django.http import FileResponse, Http404
from django.conf import settings
import os

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

if DEBUG:
    IPAddr = "http://" + IPAddr + ":8000"
else:
    IPAddr = "https://www.jinriyi.top"

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


@require_GET
def get_hot_products(request):
    infos = HotProductInfo.objects.all()
    return JsonResponse(infos, safe=False, json_dumps_params={'ensure_ascii': False})


@require_GET
def get_products(request):
    # 默认为美团平台内容
    default_listed_platform = PlatformChoice.meituan
    products = Product.objects.all()
    resp = []
    for product in products:
        listed_info = ListedInfo.objects.get(listed_platform=default_listed_platform, product=product)
        product_type = product.sub_type
        items = []
        has_items = False
        for item in resp:
            if item["product_type"] == product_type:
                items = item["detail_items"]
                has_items = True
        if not has_items:
            resp.append({
                "product_type": product_type,
                "detail_items": items
            })
        item_cont = {
            "id": product.id,
            "img_url": product.bg_img.url,
            "title": product.full_name,
            "sale_info": "月销200+",
            "praise_info": "200+觉得很赞",
            "tag_info": product.mark,
            "ori_price": product.full_price,
            "exp_price": listed_info.exp_price,
            "vip_price": product.vip_price,
            "buy_url": listed_info.bug_jump_url,
        }
        items.append(item_cont)
    print("输出内容 get_products")
    print(resp)
    return JsonResponse(resp, safe=False, json_dumps_params={'ensure_ascii': False})


@require_GET
def get_main_data(request):
    products = Product.objects.all()
    # 产品信息
    products_dic = {}
    for product in products:
        sub_type = product.sub_type
        if sub_type in products_dic:
            sub_type_proj_arr = products_dic[sub_type]
        else:
            sub_type_proj_arr = []
            products_dic[sub_type] = sub_type_proj_arr
        proj_data = {
            "img_url": IPAddr + product.bg_img.url.replace("media", "static"),
            "title": product.full_name,
            "sale_info": "月销100+",
            "praise_info": "100+觉得很赞",
            "tag_info": "立冬 养生 全身 90分钟",
            "ori_price": product.full_price,
            "exp_price": product.exp_price,
            "vip_price": product.vip_price,
            "buy_url": "../../images/shop/products/spa.png"
        }
        sub_type_proj_arr.append(proj_data)
    # 组装产品和产品分类信息
    products_data_arr = []
    sub_types = products_dic.keys()
    for sub_type in sub_types:
        sub_type_name = get_sub_type_names(sub_type)
        products_data_arr.append({
            "product_type": sub_type,
            "product_type_name": sub_type_name,
            "detail_items": products_dic[sub_type]
        })
    # 滑动图片的地址
    swiper_data = [
        IPAddr + "/media/products/images/shop/products/hanzhengfang.jpg",
        IPAddr + "/media/products/images/shop/products/hanzhengfang.jpg",
    ]
    res_data = {
        "swiper_data": swiper_data,
        "product_items": products_data_arr
    }
    print("服务器地址：", hostname)
    print("服务器地址：", IPAddr)
    return JsonResponse(res_data, safe=False, json_dumps_params={'ensure_ascii': False})


def get_sub_type_names(sub_type):
    """
    根据产品类型数字获取类型产品名字
    :param sub_type:
    :return:
    """
    for choice in ProductSubType:
        if choice.value == sub_type:
            return choice.label


def download_image(request, filename):
    print("文件名字：" + filename)
    # 获取文件路径
    file_path = os.path.join(settings.MEDIA_ROOT,  "products/images/shop/products", filename)
    print("文件路径：" + file_path)
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 以二进制模式打开文件
        file = open(file_path, 'rb')

        # 获取文件扩展名
        _, ext = os.path.splitext(filename)

        # 设置Content-Type
        content_type = 'application/octet-stream'
        if ext.lower() in ['.jpg', '.jpeg']:
            content_type = 'image/jpeg'
        elif ext.lower() == '.png':
            content_type = 'image/png'
        elif ext.lower() == '.gif':
            content_type = 'image/gif'

        # 创建FileResponse
        response = FileResponse(file, content_type=content_type)

        # 设置Content-Disposition实现下载（而不是预览）
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        # 或者设置为预览模式
        # response['Content-Disposition'] = f'inline; filename="{filename}"'

        return response
    else:
        raise Http404("文件不存在")

