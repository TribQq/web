from django.db import models

# Create your models here.

class Tabli4ka(models.Model):
    title = models.CharField('field name', max_length = 100)    # функц поля для текста <250 символов
    task = models.TextField('text') # функц поля для большого текста
    def __str__(self):
        return self.title

    class Meta: #for rename
        verbose_name = 'task' # "Select task to change" panel
        verbose_name_plural = 'tasks' #MAIN_APPLICATION panel