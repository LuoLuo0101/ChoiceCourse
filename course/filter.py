# coding:utf-8
import django_filters

__author__ = 'Luo'

from django_filters import rest_framework as filters
from .models import Enrollment


class GoodsFilter(filters.FilterSet):

    class Meta:
        model = Enrollment
        fields = ('course__name', 'course__teacher__name')
