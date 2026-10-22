from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 10  # Количество товаров на одной странице
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryPagination(PageNumberPagination):
    page_size = 5   # Количество категорий на одной странице
    page_size_query_param = 'page_size'
    max_page_size = 50
