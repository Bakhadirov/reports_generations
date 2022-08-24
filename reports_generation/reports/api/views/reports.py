from django.db import connection
from django.db.models import Count, Sum, F
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import AdminRenderer
from reports_generation.reports.api.serializers.reports import EventsSerializers, Install1Serializers, UserSerializer, \
    ReportsGenerationSerializer
from reports_generation.reports.filters import Installs1Filter, EventsFilter, ReportsViewFilter
from reports_generation.reports.models import Events, Installs1, User


class EventsViewPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500


class EventsView(ListAPIView):
    model = Events
    permission_classes = (IsAuthenticated,)
    serializer_class = EventsSerializers
    queryset = Events.objects.all()
    pagination_class = EventsViewPagination
    filterset_class = EventsFilter
    renderer_classes = [AdminRenderer]


class Installs1ViewPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500


class Installs1View(ListAPIView):
    model = Installs1
    permission_classes = (IsAuthenticated,)
    serializer_class = Install1Serializers
    queryset = Installs1.objects.all()
    pagination_class = Installs1ViewPagination
    filterset_class = Installs1Filter
    renderer_classes = [AdminRenderer]


class UserRegistrationView(CreateAPIView):
    model = User
    serializer_class = UserSerializer


class ReportsViewPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 500


class ReportsView(ListAPIView):
    # sql = "with a as (select campaign , sum(event_revenue) as event_revenue_sum, sum(event_revenue_usd) as event_revenue_usd_sum from events e group by campaign, b as (select campaign, count(event_name) as count_installs from installs1 i group by campaign) select a.campaign, a.event_revenue_sum, a.event_revenue_usd_sum, b.count_installs from a left join b on a.campaign = b.campaign)"
    # sql = 'select 1 as id, campaign, sum(event_revenue) as event_revenue_sum, sum(event_revenue_usd) as event_revenue_usd_sum from events e group by campaign'
    sql = 'select 1 as id, e.campaign , sum(e.event_revenue) as event_revenue_sum, sum(e.event_revenue_usd) as event_revenue_usd_sum, count(i.event_name) as count_installs from events e left join installs1 i  on i.campaign = e.campaign group by e.campaign'
    serializer_class = ReportsGenerationSerializer
    queryset = Events.objects.raw(sql)
    pagination_class = ReportsViewPagination
    # filterset_class = ReportsViewFilter
    renderer_classes = [AdminRenderer]

