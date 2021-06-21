from django.contrib.admin import ModelAdmin, register
from .models import *
from django.contrib.auth.models import User


@register(CharityList)
class CharityListAdmin(ModelAdmin):
    list_display = ('country', 'name')
    icon_name = 'featured_play_list'
    
@register(Donation)
class DonationAdmin(ModelAdmin):
    list_display = ('charity_list', 'user', 'amount')
    icon_name = 'attach_money'
    
@register(StoryList)
class StoryListAdmin(ModelAdmin):
    list_display = ('title', 'content', 'image')
    icon_name = 'chat'
    
    
@register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('title', 'content', 'image')
    icon_name = 'chat'   
    
     
@register(FunFact)
class FunFactAdmin(ModelAdmin):
    list_display = ('title', 'content', 'image')
    icon_name = 'chat'
   
      
@register(Participates)
class ParticipatesAdmin(ModelAdmin):
    list_display = ('user', 'image', 'approved')
    icon_name = 'person'
     
