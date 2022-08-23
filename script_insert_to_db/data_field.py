from sqlalchemy.types import String, TIMESTAMP, DECIMAL


class DFModel:
    fields = {
        'install_time': TIMESTAMP(timezone=True),
        'event_time': TIMESTAMP(timezone=True),
        'appsflyer_id': String,
        'media_source': String,
        'campaign': String,
        'platform': String,
        'event_name': String,
        'event_revenue': DECIMAL,
        'event_revenue_usd': DECIMAL
    }
