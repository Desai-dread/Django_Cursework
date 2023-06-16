from django.db import models

import Groups.models



# Create your models here.
class Tags(models.Model):
    tag_name = models.CharField("Название тега",max_length=50)
    tag_descrip = models.TextField("Описание тега" ,max_length=200)

    # descrip это сокрщ. description

    def __str__(self):
        return f'{self.tag_name}, {self.tag_descrip}'

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Squad(models.Model):
    squad_name = models.CharField("Название команды", max_length=50, null=False)
    squad_descrip = models.TextField("Описание команды", max_length=1000)
    squad_tags = models.ManyToManyField(Tags, blank=True)
    squad_abbr = models.CharField(max_length=5)
    create_date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f'{self.squad_name}, {self.squad_tags}'

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
