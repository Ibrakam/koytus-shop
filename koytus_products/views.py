from multiprocessing import context
from django.shortcuts import render

# Create your views here.
# def main(request):
#     return render(request, "index.html")

def main(request):
    products = ["Dicks", "Pussies", "Pickles", "Mangoes"]
    categories = ["Gays", "Lesbians", "Niggers", "Nikita & Ibragim"]

    return render(request, "index.html", context={"products": products, "categories": categories})




def dynamic_url(request, name):
    return render(request, "name.html", context={"name": name})

