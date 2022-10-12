from django.contrib import admin
from.models import *
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user","avatar","discription")
admin.site.register(UserProfile,UserProfileAdmin)

class ArticalAdmin(admin.ModelAdmin):
    list_display= ("title","category","Created_at",)
    search_fields=["title", "content"]
admin.site.register(Artical,ArticalAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","cover")
admin.site.register(Category, CategoryAdmin)
