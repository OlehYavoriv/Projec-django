from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    text = models.TextField('Your text')
    date = models.DateField('Date publication')


    def __str__(self):
        return f'News:{self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name_plural='News'


