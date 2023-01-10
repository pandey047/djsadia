
from django.db import models
from django.utils.html import format_html

# Create your models here.
class ResourcesCategory(models.Model):
    cat_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=100)
    category_designation=models.CharField(max_length=100)
    Category_description=models.TextField()
    url=models.CharField(max_length=100)
    image=models.ImageField(upload_to="media/resources/")
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    def image_tag(self):
        return format_html('<img src="/media/{}"style="width:40px;height:40px;border-radius:50%"/>'.format(self.image) )
    def __str__(self):
        return self.category_name


# class  Post(models.Model):
#     post_id=models.AutoField(primary_key=True) 
#     title=models.CharField(max_length=10000)
#     content=models.CharField(max_length=10000)
#     url=models.CharField(max_length=100)
#     cat=models.ForeignKey(Category,on_delete=models.CASCADE)
#     image=models.ImageField(upload_to='post/')        


class profiles(models.Model):
    category=models.ForeignKey(ResourcesCategory,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=100,default='')
    last_name=models.CharField(max_length=100,default='')
    designation=models.CharField(max_length=100,default='')
    practice_names=models.CharField(max_length=100,default='')
    education=models.TextField(default='')
    state=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    zip_code=models.IntegerField()
    address=models.CharField(max_length=100,default='')
    mobile_number=models.IntegerField()
    email_address=models.EmailField()
    introduction=models.TextField()
    speciality=models.CharField(max_length=100,default='')
    linkdin_profile=models.URLField(max_length=200)
    rating=models.IntegerField()
    # reviews=models.IntegerField()
    link=models.URLField(max_length=200)
    image=models.ImageField(upload_to='media/profile/')  
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    def image_tag(self):
        return format_html('<img src="/media/{}"style="width:40px;height:40px;border-radius:50%"/>'.format(self.image) )



    