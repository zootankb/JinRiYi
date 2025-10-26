import re, random
from feedback.models import VerificationCode
"""
全局数据操作的内容
"""


def is_valid_phone_number(phone_number):
    """
    验证手机号是否有效
    :param phone_number:
    :return:
    """
    pattern = re.compile('^1[3-9]\d{9}$')
    if pattern.match(phone_number):
        return True
    else:
        return False


def get_common_rep_data(protocol_id, msg, error_code=0):
    main_data = get_common_main_data(protocol_id, msg)
    data = {
        'data': main_data,
        'code': error_code
    }
    return data


def get_common_main_data(protocol_id, msg):
    """
    创建返回协议内容主体
    :param protocol_id: 协议号
    :param msg: 协议内容
    :return: any
    """
    data = {
        'protocol_id': protocol_id,
        'msg': msg,
    }
    return data


def get_random_verification_code():
    max_random_times = 5  # 最多随机次数
    r_num_str = None
    while max_random_times > 0:
        max_random_times -= 1
        r_num = random.randint(10000000, 99999999)
        r_num_str = str(r_num)
        if VerificationCode.objects.count() == 0:
            ver = VerificationCode()
            ver.code = r_num_str
            ver.save()
            break
        existed = VerificationCode.objects.filter(code=r_num_str, is_valid=True).count() > 0
        if not existed:
            ver = VerificationCode()
            ver.code = r_num_str
            ver.save()
            break
    return r_num_str
