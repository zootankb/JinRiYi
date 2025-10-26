from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(ShopUserInfo)
class ShopUserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'nick_name', 'mobile_phone', 'fixed_phone', 'from_platform', 'gender', 'language',
                    'city', 'province', 'country', 'avatar_url', 'description', 'mark', ]
    search_fields = ['id', 'name', 'nick_name', 'mobile_phone', 'fixed_phone', 'from_platform', 'gender', 'language',
                     'city', 'province', 'country', 'avatar_url', 'description', 'mark', ]
    list_filter = ['id', 'name', 'nick_name', 'mobile_phone', 'fixed_phone', 'from_platform', 'gender', 'language',
                   'city', 'province', 'country', 'avatar_url', 'description', 'mark', ]
    ordering = ['-id', ]
    fields = ['id', 'name', 'nick_name', 'mobile_phone', 'fixed_phone', 'from_platform', 'gender', 'language',
              'city', 'province', 'country', 'avatar_url', 'description', 'mark', ]
    readonly_fields = ['id', 'created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'mark', 'created_at']
    search_fields = ['id', 'name', 'description', 'mark', 'created_at']
    list_filter = ['id', 'name', 'description', 'mark', 'created_at']
    ordering = ['-id', ]
    fields = ['id', 'name', 'description', 'mark', 'created_at']
    readonly_fields = ['id', 'created_at']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'user', 'master_name', 'service_progress', 'master_technique', 'environment',
                    'content', 'verification_code', 'mark', 'created_at']
    search_fields = ['id', 'product', 'user', 'master_name', 'service_progress', 'master_technique', 'environment', 'content',
                     'verification_code', 'mark', 'created_at']
    list_filter = ['id', 'product', 'user', 'master_name', 'service_progress', 'master_technique', 'environment',
                   'content', 'verification_code', 'mark', 'created_at']
    ordering = ['-id', ]
    fields = ['id', 'product', 'user', 'master_name', 'service_progress', 'master_technique', 'environment', 'content',
              'verification_code', 'mark', 'created_at']
    readonly_fields = ['id', 'created_at']


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'is_valid', 'valid_time', 'mark', 'created_at']
    search_fields = ['id', 'code', 'is_valid', 'valid_time', 'mark', 'created_at']
    list_filter = ['id', 'code', 'is_valid', 'valid_time', 'mark', 'created_at']
    ordering = ['-id', ]
    fields = ['id', 'code', 'is_valid', 'valid_time', 'mark', 'created_at']
    readonly_fields = ['id', 'created_at']
