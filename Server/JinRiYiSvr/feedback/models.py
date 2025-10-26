from django.db import models
from django.contrib.auth.models import User
from datatool.enum_data import PlatformChoice, StartLevel, Gender


# Create your models here.


class ShopUserInfo(models.Model):
    id = models.AutoField("顾客ID", primary_key=True)
    name = models.CharField("名字", max_length=40, default="Null")
    nick_name = models.CharField("昵称", max_length=40, default="Null")
    mobile_phone = models.CharField("手机号", max_length=11)
    fixed_phone = models.CharField("固话", max_length=11)
    from_platform = models.CharField("来自平台", max_length=100, choices=PlatformChoice, default=PlatformChoice.wechat)
    gender = models.CharField("性别", max_length=100, choices=Gender, default=Gender.unknown)
    language = models.CharField("语言", max_length=50)
    city = models.CharField("城市", max_length=50)
    province = models.CharField("省份", max_length=50)
    country = models.CharField("国家", max_length=50)
    avatar_url = models.CharField("头像", max_length=500)
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return self.nick_name

    class Meta:
        ordering = ['-id']
        verbose_name = '顾客表'
        verbose_name_plural = '顾客表'


class Product(models.Model):
    id = models.AutoField("ID", primary_key=True)
    name = models.CharField("项目名字", max_length=40, default="Null")
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.name}"  # 在显示中包含id

    class Meta:
        ordering = ['id']
        verbose_name = '项目表'
        verbose_name_plural = '项目表'


class VerificationCode(models.Model):
    id = models.AutoField("ID", primary_key=True)
    code = models.CharField("验证码", max_length=6)
    is_valid = models.BooleanField("是否有效", default=True)
    valid_time = models.IntegerField("有效时长，单位:天", default=30)
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = '验证码'
        verbose_name_plural = '验证码'


class Feedback(models.Model):
    id = models.AutoField("ID", primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(ShopUserInfo, on_delete=models.CASCADE, null=True)
    master_name = models.CharField("师傅名字", max_length=40)
    service_progress = models.CharField("服务流程", max_length=100, choices=StartLevel, default=StartLevel.very_good)
    master_technique = models.CharField("技师手法", max_length=100, choices=StartLevel, default=StartLevel.very_good)
    environment = models.CharField("环境卫生", max_length=100, choices=StartLevel, default=StartLevel.very_good)
    content = models.TextField("反馈内容", max_length=500)
    verification_code = models.ForeignKey(VerificationCode, on_delete=models.CASCADE, null=True)
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = '反馈表'
        verbose_name_plural = '反馈表'



