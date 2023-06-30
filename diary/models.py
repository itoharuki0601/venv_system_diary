from django.db import models

from accounts.models import CustomUser


class Diary(models.Model):
    """日記モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザーID', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='備考', max_length=40)

    content = models.CharField(max_length=50,verbose_name='朝の症状', blank=True, null=True)
    photo1 = models.IntegerField(verbose_name='朝の体温', blank=True, null=True)
    photo2 = models.CharField(max_length=50,verbose_name='夜の症状', blank=True, null=True)
    photo3 = models.IntegerField(verbose_name='夜の体温', blank=True, null=True)

    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        return self.title

