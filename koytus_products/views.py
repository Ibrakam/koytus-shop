from django.shortcuts import render
from .models import Products, CategoryProduct, UserCart


def home_page(request):
    products = Products.objects.all()
    print(products)
    categories = CategoryProduct.objects.all()

    context = {"products": products, "categories": categories}
    return render(request, "index.html", context)
    # (Prosucts(id=1, pr_name="asds"), Produ)
    



def exact_product(request, id):
    # 
    product = Products.objects.get(id=id)
    
    context = {"product": product}
    return render(request, "product.html", context)


def category_product(request, id):
    category = CategoryProduct.objects.get(id=id)
    products = Products.objects.filter(pr_category=category).all()

    context = {"products": products, "category": category}
    return render(request, "category.html", context)







# Create your views here.
# def main(request):
#     return render(request, "index.html")

# def main(request):
#   products = ["Dicks", "Pussies", "Pickles", "Mangoes"]
#     cat egories = ["Gays", "Lesbians", "Niggers", "Nikita & Ibragim"]

#     return render(request, "index.html", context={"products": products, "categories": categories})




# def dynamic_url(request, name):
#     return render(request, "name.html", context={"name": name})

