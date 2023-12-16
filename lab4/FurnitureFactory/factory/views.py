from django.shortcuts import render, get_object_or_404
from .models import Furniture, FurnitureCategory, FurnitureCollection
from cart.forms import CartAddProductForm
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import ProductForm
from django.core.exceptions import PermissionDenied
from login.models import ClientUser
from articles.models import Article
import requests




def product_list(request, product_type_name=None):
    product_type = None
    types = FurnitureCategory.objects.all()
    products = Furniture.objects.all()

    if product_type_name:
        product_type = get_object_or_404(FurnitureCategory, category=product_type_name)
        products = products.filter(category=product_type)

    sort = request.GET.get('sort')
    if sort == 'ascending':
        products = products.order_by('price')
    elif sort == 'descending':
        products = products.order_by('-price')

    return render(request, 'factory/product/list.html',
                  {
                      'type': type,
                      'types': types,
                      'products': products,
                  })

def product_list_collection(request, product_collection_name=None):
    product_type = None
    types = FurnitureCollection.objects.all()
    products = Furniture.objects.all()

    if product_collection_name:
        product_collection = get_object_or_404(FurnitureCollection, collection=product_collection_name)
        products = products.filter(collection=product_collection)

    sort = request.GET.get('sort')
    if sort == 'ascending':
        products = products.order_by('price')
    elif sort == 'descending':
        products = products.order_by('-price')

    return render(request, 'factory/product/list.html',
                  {
                      'type': type,
                      'types': types,
                      'products': products,
                  })


def product_detail(request, id):
    product = get_object_or_404(Furniture, id=id)
    cart_product_form = CartAddProductForm()


    return render(request, 'factory/product/detail.html', {'product': product,
                                                         'cart_product_form': cart_product_form})
#


def product_create(request):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    form = ProductForm()

    if request.method == "POST":

        product = Furniture.objects.create(name=request.POST.get('name'),
                                           price=request.POST.get('price'),
                                           code=request.POST.get('code'),
                                           image=request.FILES.get('image'),
                                           description=request.POST.get('description'),
                                           category=FurnitureCategory.objects.get(id=request.POST.get('category')),
                                           collection=FurnitureCollection.objects.get(id=request.POST.get('collection')),
                                           quantity=0,
                                           attributes=request.POST.get('attributes'))

        product.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "factory/product/create.html", {"form": form})


def product_edit(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    try:

        product = Furniture.objects.get(id=id)
        form = ProductForm(initial={'name': product.name, 'price': product.price, 'code': product.code,
                                    'image': product.image, 'category': product.category,
                                    'collection': product.collection, 'description': product.description,
                                    'attributes': product.attributes})

        if request.method == "POST":
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.category = Furniture.objects.get(id=request.POST.get('category'))
            product.collection = FurnitureCategory.objects.get(id=request.POST.get('collection'))
            product.image = request.FILES.get('image')
            product.description = request.POST.get('description')

            product.attributes = request.POST.get('attributes')

            product.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "factory/product/edit.html", {"product": product, "form": form})
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>product not found</h2>")


def product_delete(request, id):
    """
    deleting data in estate base
    """
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    try:

        product = Furniture.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/")
    except product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def about(request):
    return render(request, 'templateslab1/about_company.html')
def lab3(request):
    return render(request, 'templateslab1/lab3.html')


def contacts(request):

    staff = ClientUser.objects.filter(is_staff=True)
    context = {'staff': staff}
    for member in staff:
        print(member.image)

    return render(request, 'templateslab1/contacts.html', context)


def guest(request):
    article = Article.objects.all().order_by('-created')[0]
    return render(request, 'templateslab1/guest_page.html', {'article':article})


def privacy_policy(request):
    return render(request, 'templateslab1/privacy_policy.html')


