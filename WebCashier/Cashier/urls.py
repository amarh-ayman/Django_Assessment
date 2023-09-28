from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListCreateView, ProductDetailView, PayAPIView, TransactionsReportView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('pay/', PayAPIView.as_view(), name='pay'),
    path('transactions/', TransactionsReportView.as_view(), name='transactions-report'),
]