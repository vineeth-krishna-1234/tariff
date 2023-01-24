from django.db import models




class food_details(models.Model):
    item_name= models.CharField(max_length=40)
    avilable_quantity=models.IntegerField(default=0)
    price=models.IntegerField(blank=False, null=False)
    item_image=models.ImageField(upload_to='images/',max_length=255)
    serve_type=models.CharField(max_length=50,choices=[
    ("Breakfast","breakfast"),
    ("Lunch","dinner"),
    ("Dinner","dinner")],
    default="Breakfast"
    )
    def __str__(self):
        return  self.item_name+"| quantity:"+str(self.avilable_quantity)