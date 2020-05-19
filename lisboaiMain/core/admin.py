from django.contrib import messages, admin
from lisboaiMain.core.models import Categories,Article,Social, Post
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html


admin.site.site_header = 'Fora do box - Admin'

class CategoriesAdmin(admin.ModelAdmin):
    fields = (
        'name', 
        'nameUrl'
        )
    list_display = (
        'name',
        )
    readonly_fields = [
        'nameUrl'
        ] 
admin.site.register(Categories, CategoriesAdmin)

def make_published(modeladmin, request, queryset):
    queryset.update(state='p')
    make_published.short_description = "Mark selected stories as published"

def make_draft(modeladmin, request, queryset):
    queryset.update(state='d')
    make_draft.short_description = "Mark selected stories as draft"


class ArticleAdmin(SummernoteModelAdmin):
    
    fields = (
        'categories',
        'title',
        'slug',
        'short_description',
        'image',
        'body',
        'state',
        'created_by',
        'spotlight', 
        )
    list_display = (
        'title',
        'categories',
        'state',
        'updated',
        'spotlight'
        )
    prepopulated_fields = {
        'slug': ('title',)
        }
    summernote_fields = (
        'body',
        )
    readonly_fields = [
        'state'
        ] 
    actions = [make_published, make_draft]
    list_filter = [
        'spotlight'
        ] 
    list_editable = (
        'spotlight',
        )

    def save(self, *args, **kwargs):
        vote_count = Article.objects.filter(spotlight=True).count()
        messages.warning('Você ja tem 2 destaques cadastrados')
        
        super(Article, self).save(*args, **kwargs) 
    
admin.site.register(Article, ArticleAdmin)


class SocialAdmin(admin.ModelAdmin):
    fields = (
        'name', 
        'link',
        'icon'
        )
    list_display = (
        'name', 
        'link',
        'icon'
        )
admin.site.register(Social, SocialAdmin)
 

class PostAdmin(admin.ModelAdmin):

    fields = (
        'name', 
        'email',
        'message'
        )
admin.site.register(Post, PostAdmin)



