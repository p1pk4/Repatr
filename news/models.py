from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=15)
    hashtag = models.CharField('Хештег', max_length=20)
    full_text = models.TextField('Текст')
    # date = models.DateField('Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        """ Переадресация пользователя после редактирования/удаления статьи """
        return f'/news/{self.id}'

    def __str__(self):
        return f'{self.title} - #{self.hashtag}'
