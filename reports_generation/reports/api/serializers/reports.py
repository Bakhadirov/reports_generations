from django.contrib.auth import get_user_model
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from typing import Dict, Any
from reports_generation.reports.models import Events, Installs1, User

UserModel = get_user_model()


class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ( 'install_time',
                  'event_time',
                  'appsflyer_id',
                  'media_source',
                  'campaign',
                  'platform',
                  'event_name',
                  'event_revenue',
                  'event_revenue_usd',)


class Install1Serializers(serializers.ModelSerializer):
    class Meta:
        model = Installs1
        fields = ('id',
                  'install_time',
                  'event_time',
                  'appsflyer_id',
                  'media_source',
                  'campaign',
                  'platform',
                  'event_name',
                  'event_revenue',
                  'event_revenue_usd',)


class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'},
    )

    def create(self, validated_data: Dict[str, Any]) -> Dict[str, Any]:
        validated_data['password'], _ = validated_data.pop('password1'), validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
        model = User
        fields = (
            'id',
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'patronymic',
            'extra_information',
        )

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        if attrs['password1'] != attrs['password2']:
            raise ValidationError('Passwords don\'t match; Пароли не совпадают')

        return attrs


class ReportsGenerationSerializer(serializers.Serializer):
    campaign = serializers.CharField(max_length=255)
    event_revenue_sum = serializers.IntegerField(allow_null = True)
    event_revenue_usd_sum = serializers.IntegerField(allow_null = True)
    count_installs = serializers.IntegerField(allow_null = True)

    class Meta:
        model = Events
        fields = ('campaign', 'event_revenue_sum', 'event_revenue_usd_sum', 'count_installs')

        # Post.objects.annotate(
#             viewers_count= Count('viewers', distinct=True),
#             liked_count = Count('liked', distinct=True),
#             author_in_user_following=Exists(this_user.following.filter(id=OuterRef('author_id'))), # Thx to Nikolay Cherniy
#             is_user_liked_post=Exists(this_user.liked.filter(id=OuterRef('id'))))\
#             .select_related('author','author__profile')\
#             .prefetch_related('images')\
#             .order_by('-created_at')
#
# :)
