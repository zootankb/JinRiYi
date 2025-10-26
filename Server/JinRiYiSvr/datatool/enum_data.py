from django.db import models


class PlatformChoice(models.IntegerChoices):
    wechat = 1, "微信"
    qq = 2, "QQ"
    offline = 3, "线下"
    dazhongdianping = 4, "大众点评"
    douyin = 5, "抖音"
    bilibili = 6, "B站"
    kuaishou = 7, "快手"
    xigua = 8, "西瓜"
    wechatvideo = 9, "微视"


class Gender(models.IntegerChoices):
    unknown = 0, "未知"
    man = 1, "男性"
    female = 2, "女性"


class StartLevel(models.IntegerChoices):
    not_good = 1, "不好"
    normal = 2, "一般"
    good = 3, "很好"
    very_good = 4, "非常好"
