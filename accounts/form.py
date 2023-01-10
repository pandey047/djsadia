
'''
for custom user
'''
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import UserProfile

class UserProfileCreationForm(UserCreationForm):
  class Meta:
    model = UserProfile
    fields = ("email",)
    
    
class UserProfileChangeForm(UserChangeForm):
  class Meta:
    model = UserProfile
    fields = ("email",)