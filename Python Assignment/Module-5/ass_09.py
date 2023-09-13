"""
Product_mst table with product id as primary key

o Admin can add product subcategory details Like (Product price, product image, Product model, product Ram) 
  data should store in Product_sub_cat table 

o Admin can get product name as foreign key from product_mst table in product_sub_category_details page
  Admin can view, update and delete all registered details of product manager can search product on search bar
  and get all details about product

"""
"""

MODEL.PY

        class ProductSubcategory(models.Model):
            product = models.ForeignKey('Product', on_delete=models.CASCADE)
            price = models.DecimalField(max_digits=10, decimal_places=2)
            image = models.ImageField(upload_to='product_images/', null=True, blank=True)
            model = models.CharField(max_length=100)
            ram = models.CharField(max_length=50)

            def __str__(self):
                return self.product.product_name

ADMIN.PY

        admin.site.register(ProductSubcategory)

VIWES.PY

        
    def product_subcategory_list(request):
        subcategories = ProductSubcategory.objects.all()
        return render(request, 'product_manager/product_subcategory_list.html', {'subcategories': subcategories})
  

"""