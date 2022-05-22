from django.db import models
from .utilities import get_timestamp_path



# i cant add commercial backend logick to open source -_-(описание поч для бэка)
# and much more...
class PortfolioProjectCard(models.Model):
    name = models.CharField(max_length=20)
    logo_img = models.FileField(upload_to=get_timestamp_path, verbose_name='Project logo img')
    cover_img = models.ImageField(upload_to=get_timestamp_path, verbose_name='Project cover img')# card bacground img # 416 328 # 1171 919
    project_type = models.CharField(max_length=15)#landing/intenet store
    web_version_link = models.TextField(null=True, blank=True, max_length=100) # link on wroked exeample
    # git_link = models.TextField(null=True, blank=True, max_length=100) # link on github/lab/etc (need fix template for add)
    description = models.TextField(max_length=150)
    sort_index = models.IntegerField(default=1)
    slowly_redirect = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sort_index}-{self.name} ({self.project_type})'


class PortfolioSkillCard(models.Model):
    cover_img = models.FileField(upload_to=get_timestamp_path, verbose_name='tech icon ')  # filefield for svg imgs
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    sort_index = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.sort_index}-{self.name}'

# "{{project.cover_img}}"
# ="/media/{{card.cover_img}}"