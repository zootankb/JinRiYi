from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(CustomerInfo)
class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'nick_name', 'real_name', 'mobile_phone', 'fixed_phone', 'from_platform', 'gender', 'language',
                    'city', 'province', 'country', 'avatar_url', 'is_vip', 'recharge_amount', 'description', 'mark',  'updated_at']
    search_fields = ['id', 'name', 'nick_name', 'real_name', 'mobile_phone', 'fixed_phone', 'from_platform', 'gender', 'language',
                     'city', 'province', 'country', 'avatar_url', 'is_vip', 'recharge_amount', 'description', 'mark',  'updated_at']
    list_filter = ['id', 'name', 'nick_name', 'real_name', 'mobile_phone', 'fixed_phone', 'from_platform', 'gender', 'language',
                   'city', 'province', 'country', 'avatar_url', 'is_vip', 'recharge_amount', 'description', 'mark',  'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'name', 'nick_name', 'real_name', 'mobile_phone', 'fixed_phone', 'from_platform', 'gender', 'language',
              'city', 'province', 'country', 'avatar_url', 'is_vip', 'recharge_amount', 'description', 'mark',  'updated_at']
    readonly_fields = ['id', 'created_at',  'updated_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'full_name', 'use_type', 'frequency_count', 'full_price', 'discount_number', 'final_price',
                    'on_the_shelf', 'description', 'mark', 'created_at', 'updated_at']
    search_fields = ['id', 'name', 'full_name', 'use_type', 'frequency_count', 'full_price', 'discount_number', 'final_price',
                    'on_the_shelf', 'description', 'mark', 'created_at', 'updated_at']
    list_filter = ['id', 'name', 'full_name', 'use_type', 'frequency_count', 'full_price', 'discount_number', 'final_price',
                    'on_the_shelf', 'description', 'mark', 'created_at', 'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'name', 'full_name', 'use_type', 'frequency_count', 'full_price', 'discount_number', 'final_price',
                    'on_the_shelf', 'description', 'mark', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(MasterInfo)
class MasterInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'nick_name', 'number_ticket', 'gender', 'date_of_entry', 'date_of_departure', 'at_post',
                    'mark', 'created_at', 'updated_at']
    search_fields = ['id', 'name', 'nick_name', 'number_ticket', 'gender', 'date_of_entry', 'date_of_departure', 'at_post',
                     'mark', 'created_at', 'updated_at']
    list_filter = ['id', 'name', 'nick_name', 'number_ticket', 'gender', 'date_of_entry', 'date_of_departure', 'at_post',
                   'mark', 'created_at', 'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'name', 'nick_name', 'number_ticket', 'gender', 'date_of_entry', 'date_of_departure', 'at_post',
              'mark', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'is_valid', 'valid_time', 'mark', 'created_at', 'updated_at']
    search_fields = ['id', 'code', 'is_valid', 'valid_time', 'mark', 'created_at', 'updated_at']
    list_filter = ['id', 'code', 'is_valid', 'valid_time', 'mark', 'created_at', 'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'code', 'is_valid', 'valid_time', 'mark', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'master_name', 'service_progress', 'master_technique', 'environment',
                    'content', 'verification_code', 'mark', 'created_at', 'updated_at']
    search_fields = ['id', 'product', 'user', 'master_name', 'service_progress', 'master_technique', 'environment', 'content',
                     'verification_code', 'mark', 'created_at', 'updated_at']
    list_filter = ['id', 'product', 'user', 'master_name', 'service_progress', 'master_technique', 'environment',
                   'content', 'verification_code', 'mark', 'created_at', 'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'product', 'user', 'master_name', 'service_progress', 'master_technique', 'environment', 'content',
              'verification_code', 'mark', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'received_money', 'received_count',
                    'used_end', 'mark', 'created_at', 'updated_at']
    search_fields = ['id', 'customer', 'product', 'received_money', 'received_count',
                     'used_end', 'mark', 'created_at', 'updated_at']
    list_filter = ['id', 'customer', 'product', 'received_money', 'received_count',
                   'used_end', 'mark', 'created_at', 'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'customer', 'product', 'received_money', 'received_count',
              'used_end', 'mark', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at',]


@admin.register(ConsumptionRecord)
class ConsumptionRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'real_customer', 'order1', 'order2', 'order3', 'order4', 'order5',
                     'order_time_1_start', 'order_time_1_end', 'order_time_2_start', 'order_time_2_end',
                     'order_time_3_start', 'order_time_3_end', 'order_time_4_start', 'order_time_4_end',
                     'order_time_5_start', 'order_time_5_end',
                     'consumption_1_type', 'consumption_2_type', 'consumption_3_type', 'consumption_4_type', 'consumption_5_type',
                     'order_1_master', 'order_2_master', 'order_3_master', 'order_4_master', 'order_5_master',
                     'mark', 'created_at', 'updated_at']
    search_fields = ['id', 'real_customer', 'order1', 'order2', 'order3', 'order4', 'order5',
                     'order_time_1_start', 'order_time_1_end', 'order_time_2_start', 'order_time_2_end',
                     'order_time_3_start', 'order_time_3_end', 'order_time_4_start', 'order_time_4_end',
                     'order_time_5_start', 'order_time_5_end',
                     'consumption_1_type', 'consumption_2_type', 'consumption_3_type', 'consumption_4_type', 'consumption_5_type',
                     'order_1_master', 'order_2_master', 'order_3_master', 'order_4_master', 'order_5_master',
                     'mark', 'created_at', 'updated_at']
    list_filter = ['id', 'real_customer', 'order1', 'order2', 'order3', 'order4', 'order5',
                     'order_time_1_start', 'order_time_1_end', 'order_time_2_start', 'order_time_2_end',
                     'order_time_3_start', 'order_time_3_end', 'order_time_4_start', 'order_time_4_end',
                     'order_time_5_start', 'order_time_5_end',
                     'consumption_1_type', 'consumption_2_type', 'consumption_3_type', 'consumption_4_type', 'consumption_5_type',
                     'order_1_master', 'order_2_master', 'order_3_master', 'order_4_master', 'order_5_master',
                     'mark', 'created_at', 'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'real_customer', 'order1', 'order2', 'order3', 'order4', 'order5',
                     'order_time_1_start', 'order_time_1_end', 'order_time_2_start', 'order_time_2_end',
                     'order_time_3_start', 'order_time_3_end', 'order_time_4_start', 'order_time_4_end',
                     'order_time_5_start', 'order_time_5_end',
                     'consumption_1_type', 'consumption_2_type', 'consumption_3_type', 'consumption_4_type', 'consumption_5_type',
                     'order_1_master', 'order_2_master', 'order_3_master', 'order_4_master', 'order_5_master',
                     'mark', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at',]


@admin.register(OptionRecord)
class OptionRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'mark', 'created_at', 'updated_at']
    search_fields = ['id', 'content', 'mark', 'created_at', 'updated_at']
    list_filter = ['id', 'content', 'mark', 'created_at', 'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'content', 'mark', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(RechargeRecord)
class RechargeRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'amount', 'mark', 'created_at', 'updated_at']
    search_fields = ['id', 'customer', 'amount', 'mark', 'created_at', 'updated_at']
    list_filter = ['id', 'customer', 'amount', 'mark', 'created_at', 'updated_at']
    ordering = ['-id', ]
    fields = ['id', 'customer', 'amount', 'mark', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']
