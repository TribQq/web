
# from whitenoise import WhiteNoise
import os
from django.core.wsgi import get_wsgi_application
# from whitenoise.djnago import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
# application = WhiteNoise(application, root="")
# application.add_files("", prefix="more-files/")

# application = DjangoWhiteNoise(application)
