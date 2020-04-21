from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 视图是一个函数
# 必须传一个参数，request请求对象，里面有用户发送的请求的信息，url和其他数据


from goods.models import GoodsCategory, GoodsInfo


def index(request):
    '''查询商品分类；从每个分类中获取4个商品'''
    categories = GoodsCategory.objects.all()
    for cag in categories:
        # GoodsInfo.objects.filter(goods_cag=cag)
        # 一对多的关系，查询多的一方，会在一的这一方多一个属性：多的一方的模型类名小写_set  cag.goodsinfo_set.all()
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]
    # 获取购物车里的商品 cookie key:value 商品的id:数量 cookie存的都是字符串
    cart_goods_list = []
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 通过判断id是否是数字来验证是否为商品数据
        if not goods_id.isdigit():
            continue
        # 获取当前遍历到的商品对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        # 把商品存到列表里
        cart_goods_list.append(cart_goods)
        # 累加所有商品的数量，goods_num是字符串
        cart_goods_count = cart_goods_count + int(goods_num)

    # 参数一 request，参数二 需要返回的html页面， 参数三 要传到模板里的数据
    return render(request, 'index.html', {'categories': categories,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count})

def detail(request):
    '''商品详情页面'''
    # 1 商品的分类
    categories = GoodsCategory.objects.all()
    # 2 购物车数据
    # 所有购物车商品
    cart_goods_list = []
    # 购物车商品的总数量
    cart_goods_count = 0
    # 去cookie取数据 goods_id:count
    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        # 根据id查询商品
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 把商品数量 存放到商品的对象里
        cart_goods.goods_num = goods_num
        # 把商品添加到列表里
        cart_goods_list.append(cart_goods)
        # 累加所有商品数量 得到总数量
        cart_goods_count = cart_goods_count + int(goods_num)
    # 3 当前要显示的商品数据
    # 获取传过来的商品的id
    goods_id = request.GET.get('id', 1)
    # 当前要显示的商品数据
    goods_data = GoodsInfo.objects.get(id=goods_id)
    return render(request, 'detail.html', {'categories': categories,
                                           'cart_goods_list': cart_goods_list,
                                           'cart_goods_count': cart_goods_count,
                                           'goods_data': goods_data})

def goods(request):
    '''商品分类页面'''
    # 获取传过来的分类id
    cag_id = request.GET.get('cag', 1)
    # 获取当前页码
    page_id = request.GET.get('page', 1)
    # 获取当前分类对象
    current_cag = GoodsCategory.objects.get(id=cag_id)

    # 获取当前分类对象的所有商品三种方法
    goods_data = current_cag.goodsinfo_set.all()
    # GoodsInfo.objects.filter(goods_cag=current_cag)
    # GoodsInfo.objects.filter(goods_cag_id=current_cag)

    # 实例化Paginator分页器对象，参1是需要分页的数据，参2是每一页显示的数量
    # 分页器含有分页的所有信息
    paginator = Paginator(goods_data, 12)
    page_data = paginator.page(page_id)
    # 所有分类
    categories = GoodsCategory.objects.all()
    # 购物车
    cart_goods_list = []
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 通过判断id是否是数字来验证是否为商品数据
        if not goods_id.isdigit():
            continue
        # 获取当前遍历到的商品对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        # 把商品存到列表里
        cart_goods_list.append(cart_goods)
        # 累加所有商品的数量，goods_num是字符串
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'goods.html', {'current_cag': current_cag,
                                          'page_data': page_data,
                                          'categories': categories,
                                          'cart_goods_list': cart_goods_list,
                                          'paginator': paginator,
                                          'cag_id': cag_id,
                                          'cart_goods_count': cart_goods_count, })

def testfilter(req):
    '''过滤器案例'''
    dict = {'a': 20, 'list': [1, 2, 3, 4, 5, 6]}
    return render(req, 'testfilter.html', dict)

def test(request):
    # a = 1/0
    return HttpResponse("testok")