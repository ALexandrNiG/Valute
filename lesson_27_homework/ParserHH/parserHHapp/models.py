
from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey
from django.db.models import ManyToManyField, URLField, FloatField, IntegerField




class Word(Model):
    word = CharField(max_length=30, verbose_name='Запрос')
    count = IntegerField(verbose_name='Количество')
    up = FloatField(verbose_name="Верхняя граница")
    down = FloatField(verbose_name='Нижняя граница')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Текст запроса'
        verbose_name_plural = 'Запросы'

class Skill(Model):
        name = CharField(max_length=50, verbose_name='Навык')

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = 'Название навыка'
            verbose_name_plural = 'Навыки'


class Wordskill(Model):
        id_word = ForeignKey(Word, on_delete=models.CASCADE)
        id_skill = ForeignKey(Skill, on_delete=models.CASCADE)
        count = FloatField()
        percent = FloatField()

class Type(Model):
    name = CharField(max_length=10, unique=True)


class Vacancy(Model):
    published = DateTimeField()
    name = CharField(max_length=50)
    url = URLField()
    word_id = ForeignKey(Word, on_delete=models.CASCADE)
    # area = ForeignKey(Area, on_delete=models.CASCADE)
    # schedule = ForeignKey(Schedule, on_delete=models.CASCADE)
    snippet = TextField()
    salaryFrom = FloatField(default=0)
    salaryTo = FloatField(default=0)
    # employer = ForeignKey(Employer, on_delete=models.CASCADE)
    type = ForeignKey(Type, on_delete=models.CASCADE)