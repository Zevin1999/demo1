"""ttsx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from cart.views import add_cart, show_cart, remove_cart, testcsrf, place_order, submit_order, submit_success
from goods.views import index, detail, goods, testfilter, test

urlpatterns = [
    path('admin/', admin.site.urls),
    #主页
    re_path(r'^index/$', index),
    #详情页
    re_path(r'^detail/$', detail),
    #添加到购物车
    re_path(r'cart/add_cart/$', add_cart),
    #商品分类页面
    re_path(r'^goods/$', goods),
    #购物车页面
    re_path(r'cart/show_cart/$', show_cart),
    #购物车删除商品
    re_path(r'cart/remove_cart/$', remove_cart),
    #提交订单页面
    re_path(r'cart/place_order/$', place_order),
    #提交订单功能
    re_path(r'cart/submit_order/$', submit_order),
    re_path(r'cart/submit_success/$', submit_success),
    #测试csrf
    re_path(r'^testcsrf/$', testcsrf),
    #测试过滤器
    re_path(r'^testfilter/$', testfilter),
    #中间件
    re_path(r'^test/$', test),
]
