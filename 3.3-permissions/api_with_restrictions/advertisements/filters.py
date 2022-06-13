from django_filters import rest_framework as filters, DateFromToRangeFilter, ChoiceFilter, CharFilter, ModelChoiceFilter
from rest_framework.authtoken.admin import User

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()
    status = ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    creator = ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at', 'updated_at']
