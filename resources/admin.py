from django.contrib import admin
from .models import ResourcesCategory ,profiles

# Register your models here.
class ResourcesCategoryAdmin(admin.ModelAdmin):
     list_display=('cat_id','category_name','category_designation','url','image','add_date','image_tag')
     search_fields=('CategoryOccupation',)

admin.site.register(ResourcesCategory,ResourcesCategoryAdmin) 

class ProfileAdmin(admin.ModelAdmin):
     #  list_display=('profile_firstname','profile_lastname','profile_address','profile_occupation','profile_zipcode')
     #  search_fields=('profile_firstname',)
      list_display=('first_name','state','city','designation','zip_code','image_tag')
      search_fields=('first_name',)
      list_filter=('category','zip_code','state','city')
      list_per_page=10

admin.site.register(profiles,ProfileAdmin)     
