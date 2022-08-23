import os
from pathlib import Path
from split_settings.tools import optional, include
from dotenv import load_dotenv

load_dotenv()

include(
    'project_settings/installed_apps.py',
    'project_settings/base.py',
    'project_settings/database.py',
    'project_settings/internationalization.py',
    'project_settings/staticfiles.py',
    optional('local_settings.py'),
)


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY')
SITE_ID = 1
