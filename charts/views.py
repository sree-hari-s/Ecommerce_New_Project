from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, F, Sum, Avg
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse

from orders.models import *
from .utils import *


def get_filter_options(request):
    grouped_purchases = (
        OrderProduct.objects.annotate(year=ExtractYear("order__created_at"))
        .values("year")
        .order_by("-year")
        .distinct()
    )
    options = [purchase["year"] for purchase in grouped_purchases]
    
    return JsonResponse(
        {
            "options": options,
        }
    )


def get_sales_chart(request, year):
    purchases = OrderProduct.objects.annotate(
        year=ExtractYear("order__created_at"))
    grouped_purchases = (
        purchases.annotate(month=ExtractMonth("order__created_at"))
        .values("month")
        .annotate(average=Sum("product_price"))
        .values("month", "average")
        .order_by("month")
    )
    sales_dict = get_year_dict()

    for group in grouped_purchases:
        sales_dict[months[group["month"] - 1]] = round(group["average"], 2)

    return JsonResponse(
        {
            "title": f"Sales in {year}",
            "data": {
                "labels": list(sales_dict.keys()),
                "datasets": [
                    {
                        "label": "Amount (Rs)",
                        "backgroundColor": colorPrimary,
                        "borderColor": colorPrimary,
                        "data": list(sales_dict.values()),
                    }
                ],
            },
        }
    )


def spend_per_customer_chart(request, year):
    purchases = OrderProduct.objects.annotate(
        year=ExtractYear("order__created_at"))
    grouped_purchases = (
        purchases.annotate(month=ExtractMonth("order__created_at"))
        .values("month")
        .annotate(average=Avg("product_price"))
        .values("month", "average")
        .order_by("month")
    )
    spend_per_customer_dict = get_year_dict()

    for group in grouped_purchases:
        spend_per_customer_dict[months[group["month"] - 1]] = round(group["average"], 2)
    
    
    return JsonResponse(
        {
            "title": f"Spend per customer in {year}",
            "data": {
                "labels": list(spend_per_customer_dict.keys()),
                "datasets": [
                    {
                        "label": "Amount (Rs)",
                        "backgroundColor": colorPrimary,
                        "borderColor": colorPrimary,
                        "data": list(spend_per_customer_dict.values()),
                    }
                ],
            },
        }
    )


def payment_success_chart(request, year):
    purchases = OrderProduct.objects.annotate(
        year=ExtractYear("order__created_at"))

    return JsonResponse(
        {
            "title": f"Payment success rate in {year}",
            "data": {
                "labels": [ "Placed", "Delivered", "Cancelled"],
                "datasets": [
                    {
                        "label": "Amount (Rs)",
                        "backgroundColor": [colorSuccess, colorDanger, colorPrimary,],
                        "borderColor": [colorSuccess, colorDanger, colorPrimary],
                        "data": [
                            
                            purchases.filter(order__status='Placed').count(),
                            purchases.filter(
                                order__status='Delivered').count(),
                            purchases.filter(
                                order__status='Cancelled').count(),
                            
                        ],
                    }
                ],
            },
        }
    )
