# Make Django application to demonstrate following things o There will be 2 modules(Admin,Product manager) o Admin can add product name (ex.Product id and product name) ex. (1, Samsung), (2, Apple)...etc. Data should store in
"""
MODEL.PY

    from django.db import models

    class Product(models.Model):
        product_id = models.AutoField(primary_key=True)
        product_name = models.CharField(max_length=100)

        def __str__(self):
            return self.product_name


            
ADMIN.PY

    admin.site.register(Product)

VIWES.PY

    def product_list(request):
        products = Product.objects.all()
        return render(request, 'product_manager/product_list.html', {'products': products})

URLS.PY

    urlpatterns = [
    
    path('products/', views.product_list, name='product_list'),
    
    ]

"""