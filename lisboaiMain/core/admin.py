from django.contrib import admin
from lisboaiMain.core.models import Categories,Article,Social
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html


admin.site.site_header = 'Fora do box - Admin'
class CategoriesAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
admin.site.register(Categories, CategoriesAdmin)




class ArticleAdmin(SummernoteModelAdmin):
    
    fields = ('categories','title','slug','short_description','image' ,'body','state','created_by','spotlight','body_preview', )
    list_display = ('title','categories','state','updated','spotlight')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
    readonly_fields = ('body_preview',)

    def countSpotlight(self):
        valueCount = Article.related_set.filter(spotlight=True).count()
        print(valueCount)
        return valueCount
        

admin.site.register(Article, ArticleAdmin)


class SocialAdmin(admin.ModelAdmin):
    fields = ('name', 'link','icon')
    list_display = ('name', 'link','icon')
admin.site.register(Social, SocialAdmin)
 