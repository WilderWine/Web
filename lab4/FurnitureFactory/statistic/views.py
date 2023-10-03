import matplotlib
import os
import matplotlib.pyplot as plt

from factory.models import Furniture, FurnitureCategory, FurnitureCollection
from .forms import StatisticForm
from django.shortcuts import render, get_object_or_404
from order.models import Order, OrderItem
from django.conf import settings
from django.core.exceptions import PermissionDenied
from typing import Dict

matplotlib.use('Agg')


def statistic_show(request):
    """
    showing statistic according show
    """
    if not request.user.is_superuser:
        raise PermissionDenied("You do not have access to this page.")

    form = StatisticForm()
    pt = dict()

    x = []
    y = []

    for ord in Order.objects.all():
        pt[str(ord.created.year) + '.' + str(ord.created.month) + '.' + str(ord.created.day)] = 0

    for ord in Order.objects.all():
        pt[str(ord.created.year) + '.' + str(ord.created.month) + '.' + str(ord.created.day)] += 1

    for tmp in pt:
        x.append(tmp)
        y.append(pt[tmp])

    plt.plot(x, y, 'ro')

    if request.method == "GET":
        plt.savefig(os.path.join(settings.MEDIA_ROOT, 'schedule.jpg'), format='jpg')
        plt.clf()
        return render(request, 'statistic/statistic.html')


def tables_show(request):
    """
    showing table statistic
    """
    if not request.user.is_superuser:
        raise PermissionDenied("You do not have access to this page.")

    # table estate - owner
    product_list = list(Furniture.objects.all())
    product_list.sort(key=lambda x: x.purchase_count, reverse=True)

    # summary table
    ords = list(OrderItem.objects.all())

    dates_arr = set()

    for tmp in ords:
        dates_arr.add(tmp.order.created.date().strftime("%Y-%m-%d"))

    dates_arr = list(dates_arr)
    categ_dict: Dict[str, Dict[str, int]]
    categ_dict = dict()
    total = dict()

    coll_dict: Dict[str, Dict[str, int]]
    coll_dict = dict()
    total2 = dict()

    for tmp in ords:
        categ_dict[tmp.product.category.category] = dict()

    for tmp in ords:
        categ_dict[tmp.product.category.category][tmp.order.created.date().strftime("%Y-%m-%d")] = 0
        total[tmp.order.created.date().strftime("%Y-%m-%d")] = 0

    for tmp in ords:
        categ_dict[tmp.product.category.category][tmp.order.created.date().strftime("%Y-%m-%d")] += tmp.quantity
        total[tmp.order.created.date().strftime("%Y-%m-%d")] += tmp.quantity


    for tmp2 in ords:
        coll_dict[tmp2.product.collection.collection] = dict()

    for tmp2 in ords:
        coll_dict[tmp2.product.collection.collection][tmp2.order.created.date().strftime("%Y-%m-%d")] = 0
        total2[tmp2.order.created.date().strftime("%Y-%m-%d")] = 0

    for tmp2 in ords:
        coll_dict[tmp2.product.collection.collection][tmp2.order.created.date().strftime("%Y-%m-%d")] += tmp2.quantity
        total2[tmp2.order.created.date().strftime("%Y-%m-%d")] += tmp2.quantity


    categ_dict['total'] = total
    print(categ_dict)
    row = list()
    row.append('Category')
    for tmp in total:
        row.append(tmp)

    coll_dict['total'] = total
    row2 = list()
    row2.append('Collection')
    for tmp2 in  total2:
        row2.append(tmp)

    categ_list = list()
    categ_list.append(row)
    for tmp in categ_dict:
        row = list()
        row.append(tmp)
        for tmp1 in categ_dict[tmp]:
            row.append(categ_dict[tmp][tmp1])

        categ_list.append(row)

    coll_list = list()
    coll_list.append(row2)
    for tmp2 in coll_dict:
        row = list()
        row.append(tmp2)
        for tmp1 in coll_dict[tmp2]:
            row.append(coll_dict[tmp2][tmp1])

        coll_list.append(row)

    return render(request,
                  'statistic/tables.html',
                  context={'product_table': product_list, 'categ_table': categ_list, 'coll_table': coll_list})

'''
def predict_show(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied("You do not have access to this page.")

    name = Furniture.objects.get(id=id).name

    ords = list(OrderItem.objects.all())
    date_arr = list()
    for tmp in ords:
        if tmp.product.name == name:
            print(tmp.order.created)
            date_arr.append(tmp.order.created)

    if (len(date_arr) == 0):
        return render(request,
                      'statistic/zero_orders.html')

    min_date = min(date_arr)
    max_count = 0
    min_count = 10000
    sum = 0
    max_date = max(date_arr)

    dates_for_plot = pandas.date_range(min_date, max_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d").to_list()
    print(dates_for_plot)

    dict_for_plot = dict()

    for tmp in dates_for_plot:
        dict_for_plot[tmp] = 0

    for tmp in dates_for_plot:
        for tmp_ord in OrderItem.objects.all():
            if tmp_ord.order.created.strftime("%Y-%m-%d") == tmp:
                dict_for_plot[tmp] += tmp_ord.quantity
                max_count = max(max_count, tmp_ord.quantity)
                min_count = min(min_count, tmp_ord.quantity)
                sum += tmp_ord.quantity

    avg = (max_count + min_count) / 2
    coef = sum / len(dict_for_plot)
    coef = avg / coef
    coef -= 1  # coef evyj;fnm
    if (coef < 0):
        coef *= -1
    max_date += datetime.timedelta(days=1)
    print(pandas.date_range(max_date, periods=1, freq='d', ).strftime("%Y-%m-%d").to_list())
    sz = len(dict_for_plot)

    for i in range(sz):
        print(max_date)
        dt = pandas.date_range(max_date, periods=2, freq='d', ).strftime("%Y-%m-%d").to_list()[0]
        val = dict_for_plot[dates_for_plot[-(i - 1)]] * coef
        dict_for_plot[dt] = round((val + avg) / 2)
        max_date += datetime.timedelta(days=1)

    x_list = list()
    y_list = list()

    for tmp in dict_for_plot:
        x_list.append(tmp)
        y_list.append(dict_for_plot[tmp])

    plt.plot(x_list, y_list)
    plt.xticks(rotation=340)
    plt.savefig(os.path.join(settings.MEDIA_ROOT, 'predict.jpg'), format='jpg')
    plt.close()

    return render(request,
                  'statistic/predict.html')
'''