from django.contrib import admin
from .models import *
from markdownx.widgets import AdminMarkdownxWidget

admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理系统'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 在列表中显示那些列
    list_display = (
        'title', 'date_publish', 'user', 'isMarkdown', 'isPublish'
    )

    list_display_links = ('title',)
    list_filter = ('isPublish',)
    list_per_page = 15

    # 发布文章界面
    fieldsets = (
        ('基本信息', {
            'fields': ('title', 'content',)
        }),
        ('高级设置', {
            'classes': ('wide',),
            'fields': ('user', 'isPublish', 'isMarkdown')
        })
    )

    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

    class Media:
        css = {
            'all': ('/static/css/code.css',),
        }
