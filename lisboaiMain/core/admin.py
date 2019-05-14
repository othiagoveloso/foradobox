from django.contrib import admin
from lisboaiMain.core.models import Categories,Article,Social
from django_summernote.admin import SummernoteModelAdmin


class CategoriesAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
admin.site.register(Categories, CategoriesAdmin)




class ArticleAdmin(SummernoteModelAdmin):

    fields = ('categories','title','slug','short_description','image' ,'body','state','created_by','spotlight' )
    list_display = ('title','categories','state','updated','spotlight')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
    

admin.site.register(Article, ArticleAdmin)


class SocialAdmin(admin.ModelAdmin):
    fields = ('name', 'link','icon')
    list_display = ('name', 'link','icon')
admin.site.register(Social, SocialAdmin)
 