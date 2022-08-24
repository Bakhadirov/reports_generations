from django_filters import rest_framework as filters

from reports_generation.reports.models import Events, Installs1


class EventsFilter(filters.FilterSet):
    campaign = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Events
        fields = ('media_source', 'platform',)


class Installs1Filter(filters.FilterSet):
    campaign = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Installs1
        fields = ('media_source', 'platform',)


class ReportsViewFilter(filters.FilterSet):
    campaign = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Events
        fields = ('media_source', 'platform',)
