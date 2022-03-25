

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.djnago import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application)