import datetime

from django.db import models
from django.contrib.auth.models import User
from datatool.enum_data import PlatformChoice, StartLevel, Gender, UseType


# Create your models here.


class CustomerInfo(models.Model):
    id = models.AutoField("顾客ID", primary_key=True)
    name = models.CharField("名字", max_length=40, blank=False)
    nick_name = models.CharField("昵称", max_length=40, blank=True)
    real_name = models.CharField("真实姓名", max_length=40, blank=True)
    mobile_phone = models.CharField("手机号", max_length=11, blank=True)
    fixed_phone = models.CharField("固话", max_length=11, blank=True)
    from_platform = models.PositiveSmallIntegerField("来自平台", choices=PlatformChoice, default=PlatformChoice.unknown)
    gender = models.PositiveSmallIntegerField("性别", choices=Gender, default=Gender.unknown)
    language = models.CharField("语言", max_length=50, blank=True)
    city = models.CharField("城市", max_length=50, blank=True)
    province = models.CharField("省份", max_length=50, blank=True)
    country = models.CharField("国家", max_length=50, blank=True)
    avatar_url = models.CharField("头像", max_length=500, blank=True)
    is_vip = models.BooleanField("VIP客户", default=False)
    recharge_amount = models.FloatField("剩余金额", default=0)
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return f'{self.name} - {self.nick_name} - {self.real_name}'

    class Meta:
        ordering = ['-id']
        verbose_name = '顾客表'
        verbose_name_plural = '顾客表'


class Product(models.Model):
    id = models.AutoField("ID", primary_key=True)
    name = models.CharField("项目名字", max_length=40, blank=True)
    full_name = models.CharField("项目全称", max_length=80, blank=False)
    use_type = models.PositiveSmallIntegerField("使用类型", choices=UseType, default=UseType.once_money)
    frequency_count = models.IntegerField("次卡：次数", default=0)
    full_price = models.FloatField("定价：元", default=0)
    discount_number = models.FloatField("折扣力度：0-1.0", default=1.0)
    final_price = models.FloatField("最终价格", default=0)
    on_the_shelf = models.BooleanField("是否上架", default=True)
    description = models.TextField("介绍", max_length=400, default="无")
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return f"{self.id} - {self.name}"  # 在显示中包含id

    class Meta:
        ordering = ['id']
        verbose_name = '项目表'
        verbose_name_plural = '项目表'


class MasterInfo(models.Model):
    id = models.AutoField("ID", primary_key=True)
    name = models.CharField("名字", max_length=40, blank=False)
    nick_name = models.CharField("昵称", max_length=40, blank=True)
    number_ticket = models.IntegerField("号位", default=1)
    gender = models.PositiveSmallIntegerField("性别", choices=Gender, default=Gender.unknown)
    date_of_entry = models.DateField("入职日期", default=datetime.date.today)
    date_of_departure = models.DateField("离职日期", default=datetime.date.today)
    at_post = models.BooleanField("是否在职", default=False)
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = '师傅表'
        verbose_name_plural = '师傅表'


class VerificationCode(models.Model):
    id = models.AutoField("ID", primary_key=True)
    code = models.CharField("验证码", max_length=6)
    is_valid = models.BooleanField("是否有效", default=True)
    valid_time = models.IntegerField("有效时长，单位:天", default=30)
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['-id']
        verbose_name = '验证码'
        verbose_name_plural = '验证码'


class Feedback(models.Model):
    id = models.AutoField("ID", primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, null=True)
    master_name = models.CharField("师傅名字", max_length=40, blank=True)
    service_progress = models.PositiveSmallIntegerField("服务流程", choices=StartLevel, default=StartLevel.very_good)
    master_technique = models.PositiveSmallIntegerField("技师手法", choices=StartLevel, default=StartLevel.very_good)
    environment = models.PositiveSmallIntegerField("环境卫生", choices=StartLevel, default=StartLevel.very_good)
    content = models.TextField("反馈内容", max_length=500)
    verification_code = models.ForeignKey(VerificationCode, on_delete=models.CASCADE, null=True)
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return f"{self.id} - {self.product} - {self.content}"

    class Meta:
        ordering = ['-id']
        verbose_name = '反馈表'
        verbose_name_plural = '反馈表'


class OrderInfo(models.Model):
    id = models.AutoField("ID", primary_key=True)
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    from_platform = models.PositiveSmallIntegerField("来源", choices=PlatformChoice, default=PlatformChoice.unknown)
    received_money = models.FloatField("实收金额", default=0)
    received_count = models.IntegerField("总次数", default=0)
    used_end = models.BooleanField("是否已经使用完毕", default=False)
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return f"{self.id} - {self.customer} - {self.product} - {self.received_money} - {self.received_count}"

    class Meta:
        ordering = ['-id']
        verbose_name = '订单表'
        verbose_name_plural = '订单表'


class ConsumptionRecord(models.Model):
    id = models.AutoField("ID", primary_key=True)
    real_customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, null=True)
    order1 = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_order_field1')
    order2 = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_order_field2')
    order3 = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_order_field3')
    order4 = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_order_field4')
    order5 = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_order_field5')
    order_time_1_start = models.DateTimeField("第1个项目开始时间", default=datetime.datetime.now(), blank=True)
    order_time_1_end = models.DateTimeField("第1个项目结束时间", default=datetime.datetime.now(), blank=True)
    order_time_2_start = models.DateTimeField("第2个项目开始时间", default=datetime.datetime.now(), blank=True)
    order_time_2_end = models.DateTimeField("第2个项目结束时间", default=datetime.datetime.now(), blank=True)
    order_time_3_start = models.DateTimeField("第3个项目开始时间", default=datetime.datetime.now(), blank=True)
    order_time_3_end = models.DateTimeField("第3个项目结束时间", default=datetime.datetime.now(), blank=True)
    order_time_4_start = models.DateTimeField("第4个项目开始时间", default=datetime.datetime.now(), blank=True)
    order_time_4_end = models.DateTimeField("第4个项目结束时间", default=datetime.datetime.now(), blank=True)
    order_time_5_start = models.DateTimeField("第5个项目开始时间", default=datetime.datetime.now(), blank=True)
    order_time_5_end = models.DateTimeField("第5个项目结束时间", default=datetime.datetime.now(), blank=True)
    consumption_1_type = models.PositiveSmallIntegerField("第1个项目消费类型", choices=UseType, default=UseType.once_money)
    consumption_2_type = models.PositiveSmallIntegerField("第2个项目消费类型", choices=UseType, default=UseType.once_money)
    consumption_3_type = models.PositiveSmallIntegerField("第3个项目消费类型", choices=UseType, default=UseType.once_money)
    consumption_4_type = models.PositiveSmallIntegerField("第4个项目消费类型", choices=UseType, default=UseType.once_money)
    consumption_5_type = models.PositiveSmallIntegerField("第5个项目消费类型", choices=UseType, default=UseType.once_money)
    order_1_master = models.ForeignKey(MasterInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_master_field1')
    order_2_master = models.ForeignKey(MasterInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_master_field2')
    order_3_master = models.ForeignKey(MasterInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_master_field3')
    order_4_master = models.ForeignKey(MasterInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_master_field4')
    order_5_master = models.ForeignKey(MasterInfo, on_delete=models.CASCADE, null=True, related_name='consumption_2_master_field5')
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return f"{self.id} - {self.customer}"

    class Meta:
        ordering = ['-id']
        verbose_name = '消费记录表'
        verbose_name_plural = '消费记录表'


class OptionRecord(models.Model):
    id = models.AutoField("ID", primary_key=True)
    content = models.CharField("记录内容", max_length=2000)
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return f"{self.id} - {self.content}"

    class Meta:
        ordering = ['-id']
        verbose_name = '操作记录表'
        verbose_name_plural = '操作记录表'


class RechargeRecord(models.Model):
    id = models.AutoField("ID", primary_key=True)
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, null=True)
    amount = models.FloatField("金额", default=0)
    mark = models.TextField("备注", max_length=400, default="这个人很懒，什么都没有留下")
    created_at = models.DateTimeField("添加日期", auto_now_add=True)
    updated_at = models.DateTimeField("更新日期", auto_now=datetime.datetime.now)

    def __str__(self):
        return f"{self.customer} - {self.amount}"

    class Meta:
        ordering = ['-id']
        verbose_name = '充值记录表'
        verbose_name_plural = '充值记录表'
