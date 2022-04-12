import django_filters

from api.models import Models

class CharFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass

class DoubleFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass

class CarFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")
    # city =  CharFilter(field_name="city", lookup_expr="in")
    # transmission = CharFilter(field_name="transmission", lookup_expr="in")
    # steering = CharFilter(field_name="steering", lookup_expr="in")
    # color = CharFilter(field_name="color", lookup_expr="in")
    # drive_unit = CharFilter(field_name="drive_unit", lookup_expr="in")
    cleared_RK = django_filters.BooleanFilter(field_name="cleared_RK", lookup_expr="in")
    # description = CharFilter(field_name="description", lookup_expr="in")
    # contacts = CharFilter(field_name="contacts", lookup_expr="in")
    year = django_filters.RangeFilter()
    # brand = CharFilter(field_name="brand", lookup_expr="in")
    print(title)
    class Meta:
        model = Models
        fields = ['title', 'year']#['title', 'cleared_RK', 'year', 'brand', 'city']