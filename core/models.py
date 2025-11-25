from django.db import models

class Purchases(models.Model):
    title = models.CharField(
        max_length=200, 
        verbose_name='Название товара'
        )
    cost = models.CharField(
        max_length=200, 
        verbose_name='Стоимость'
        )
    buy_date = models.DateTimeField(
        verbose_name='Дата покупки'
        )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
        )

    # чтобы отображались красивые названия в админке
    class Meta:
        verbose_name = 'Покупки'
        verbose_name_plural = 'Покупка'

    def __str__(self):
        return self.title