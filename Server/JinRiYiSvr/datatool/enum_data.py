from django.db import models


class PlatformChoice(models.IntegerChoices):
    unknown = 0, "未知"
    meituan = 1, "美团"
    dazhongdianping = 2, "大众点评"
    douyin = 3, "抖音"
    wechat = 4, "微信"
    qq = 5, "QQ"
    offline = 6, "线下"
    bilibili = 7, "B站"
    kuaishou = 8, "快手"
    xigua = 9, "西瓜"
    wechatvideo = 10, "微视"


class Gender(models.IntegerChoices):
    unknown = 0, "未知"
    man = 1, "男性"
    female = 2, "女性"


class StartLevel(models.IntegerChoices):
    not_good = 1, "不好"
    normal = 2, "一般"
    good = 3, "很好"
    very_good = 4, "非常好"


class UseType(models.IntegerChoices):
    once_money = 1, '金额'
    frequency = 2, '次卡'

