from rest_framework import serializers
from .models import ResourcesCategory ,profiles

class ResourcesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourcesCategory
        fields = ['cat_id','category_name','category_designation','Category_description','url','image','add_date',]

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = profiles
        fields = ['category','id','first_name',"last_name",'designation','practice_names','education','state','city','zip_code','address','mobile_number','email_address','introduction','speciality','linkdin_profile','rating','link','image','add_date']
        

    #     cat=models.ForeignKey(ResourcesCategory,on_delete=models.CASCADE)
    # id=models.AutoField(primary_key=True)
    # first_name=models.CharField(max_length=100)
    # last_name=models.CharField(max_length=100)
    # occupation=models.CharField(max_length=100)
    # mobile_number=models.IntegerField()
    # email_address=models.EmailField()
    # address=models.CharField(max_length=100)
    # state=models.CharField(max_length=100,default='')
    # city=models.CharField(max_length=100,default='')
    # zip_code=models.IntegerField()
    # description=models.TextField()
    # education_background=models.TextField(default='')
    # rating=models.IntegerField()
    # image=models.ImageField(upload_to='media/profile/')  
        

   
