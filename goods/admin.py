from django.contrib import admin

# Register your models here.
from goods.models import GoodsInfo


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods_name', 'goods_price', 'goods_desc', 'desc']
    #每页显示的数量
    list_per_page = 10
    action_on_top = True
    actions_on_bottom = True
    #在界面显示搜索  列表里是搜索依赖的字段
    search_fields = ['id', 'goods_name']

admin.site.register(GoodsInfo,GoodsInfoAdmin)
