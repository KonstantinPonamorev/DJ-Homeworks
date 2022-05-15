from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTags


class ArticleTagsInlineFormset(BaseInlineFormSet):
    def check_is_main(self):
        check_dict = {}
        for form in self.forms:
            if check_dict[form.cleaned_data['article_id']]:
                raise ValidationError('Основным может быть только один раздел')
            else:
                if form.cleaned_data['is_main']:
                    check_dict[form.cleaned_data['article_id']] = True
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
    inlines = [ArticleTagsInline, ]
