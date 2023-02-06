from django.utils.html import format_html
from django.contrib import admin
from . models import Contestent, AmountReceived
# Register your models here.
admin.site.site_header = "RAWSTAR ADMINISTRATION"

class AmountReceivedAdmin(admin.ModelAdmin):
  list_display = ('contestent_id','jrnlno','amount','date')
  group_by  = 'contestent_id'
  search_fields = ('contestent_id__name', 'jrnlno', 'amount', 'date')
 

class ContestentAdmin(admin.ModelAdmin):
  list_display = ('name','voterid','dzongkhag')
  search_fields = ('name',)

admin.site.register(Contestent,ContestentAdmin)
admin.site.register(AmountReceived,AmountReceivedAdmin) 