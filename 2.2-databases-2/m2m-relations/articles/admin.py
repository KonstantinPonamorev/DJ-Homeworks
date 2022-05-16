from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTags


class ArticleTagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        Is_main = False
        for form in self.forms:
            if form.cleaned_data['is_main'] and Is_main:
                raise ValidationError('Основным может быть только один раздел')
            elif form.cleaned_data['is_main']:
                Is_main = True
            else:
                raise ValidationError('Укажите основной раздел')
        return super().check_is_main()


class ArticleTagsInline(admin.TabularInline):
    model = ArticleTags
    formset = ArticleTagsInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [ArticleTagsInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    # inlines = [ArticleTagsInline, ]
