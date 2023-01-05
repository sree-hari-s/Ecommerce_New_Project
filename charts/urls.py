from django.urls import path

from . import views

urlpatterns = [
    path('charts/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path('charts/sales/<int:year>/', views.get_sales_chart, name='chart-sales'),
    path('charts/sales/spend-per-customer/<int:year>/', views.spend_per_customer_chart, name='chart-spend-per-customer'),
    path('charts/sales/payment-success/<int:year>/', views.payment_success_chart, name='chart-payment-success'),
]