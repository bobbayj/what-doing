from django.shortcuts import render

# Create your views here.
def cgt_product_view(request, *args, **kwargs):
    return render(request, "cgtaxcalc.html", {})