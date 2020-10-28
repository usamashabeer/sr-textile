from django.db import models

# # Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    art_no = models.CharField(max_length=50, default="")
    colors = models.CharField(max_length=100, default="")
    desc=models.CharField(max_length=1000)
    image = models.ImageField(upload_to="srtextile/images", default="")
    fabric_logo = models.ImageField(upload_to="srtextile/images", default="")
    fabric = models.CharField(max_length=100, default="")
    weave = models.CharField(max_length=100, default="")
    gsm = models.CharField(max_length=100, default="")
    dyeing = models.CharField(max_length=100, default="")
    finish = models.CharField(max_length=100, default="")
    range = models.CharField(max_length=100, default="")



    def __str__(self):
        s =self.category+" "+self.art_no
        return s