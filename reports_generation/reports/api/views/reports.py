from django.db.models import Count, Sum
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import AdminRenderer
from reports_generation.reports.api.serializers.reports import EventsSerializers, Install1Serializers, UserSerializer, \
    ReportsGenerationSerializer
from reports_generation.reports.filters import Installs1Filter, EventsFilter
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


class ReportsView(ListAPIView):
    queryset = Events.objects.all()
    serializer_class = ReportsGenerationSerializer

    def get_queryset(self):
        return Events.objects.aggregate(event_revenue_sum = Sum('event_revenue'),
                                       event_revenue_usd_sum = Sum('event_revenue_usd'))

