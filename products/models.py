from django.db import models

class Menu(models.Model) :
    name = models.CharField(max_length=45)
    class Meta :
        db_table = 'menu'

class Categories(models.Model) :
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    class Meta :
        db_table = 'categories'

class Nutritions(models.Model) :
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=2)
    protein_g = models.DecimalField(max_digits=5, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)
    class Meta :
        db_table = 'nutritions'

class Allergy(models.Model) :
    name = models.CharField(max_length=45)
    class Meta :
        db_table = 'allergy'

class Products(models.Model) :
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    nutritions_id = models.ForeignKey(Nutritions, on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(max_length=2000)
    
    class Meta :
        db_table = 'products'

class Allergy_products(models.Model) :
    allergy_id = models.ForeignKey(Allergy, on_delete=models.CASCADE)
    puduct_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    class Meta :
        db_table = 'allergy_products'

class images(models.Model) :
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2000)
    class Meta :
        db_table = 'images'
