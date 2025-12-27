from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def sample(request):
    print(request)
    qp1 = request.GET.get("name")
    qp2 = request.GET.get("city")
    return HttpResponse(f"{qp1} is from {qp2}")

def sample1(request):
    info = {"data":[{"name":"raj","age":21,"city":"sklm"},{"name":"hari","age":30,"city":"sklm"}]}
    return JsonResponse(info)


def sample2 (request):
    data = [{"name":"rajendra","city":"hyderbad"},{"name":"prasad","city":"banglore"},{"name":"uma","city":"banglore"},{"name":"raghu","city":"hyderbad"}]
    filterdata = []
    for students in data:
        if students["city"] == "hyderbad":
            filterdata.append(students)
    return JsonResponse(filterdata,safe=False)

def sample3(request):
    product_name = request.GET.get("product_name","laptop")
    product_quantity = int(request.GET.get("product_quantity",2))
    product_price = int(request.GET.get("product_price",75000))
    return JsonResponse({"product name":product_name,"product quantity":product_quantity,"product price":product_price,"product_total_price":product_quantity*product_price})



def filteringdata(request):
    data = [{"name":"rajendra","city":"hyderabad"},{"name":"prasad","city":"banglore"},{"name":"uma","city":"banglore"},{"name":"raghu","city":"hyderabad"}]
    filter_data = []
    city = request.GET.get("city","hyderabad")
    filter_data = []
    for x in data:
        if x["city"] == city:
            filter_data.append(x)
    return JsonResponse(filter_data,safe=False)


def pagination(request):
    x = ['apple','banana','carrot','grapes','water melon','kiwi','pineapple','custered apple','straberry']
    page = int(request.GET.get("page",1))
    limit = int(request.GET.get("limit",3))
    start = (page-1)*limit
    end = page*limit
    total_pages = math.ceil(len(x)/limit)
    result = x[start:end]
    res = {"status":"success" ,"current_page": page,"total_pages":total_pages}
    return JsonResponse(res,status = 202)

