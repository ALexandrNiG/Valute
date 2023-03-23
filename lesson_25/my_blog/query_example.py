# Основные
# all, get, filter
# Фильтры
# 1. с одним парметром
# Post.objects.filter(name='tank')
# 2. exclude = фильтр ноаборот
# Post.objects.exclude(name='tank')
# 3. Несколько параметров
# Post.objects.filter(name='tank', text='ddd')
# 4. Можно применять любые запросы к полученому QuerySet
# >>> tanks = Post.objects.filter(name='tank')
# >>> some = tanks.filter(text='ddd')
# >>> some
# <QuerySet []>
# tanks = Post.objects.filter(name='tank').filter(text='ddd').filter(name='ggg')
# tanks = Post.objects.filter(name='tank').exclude(text='ddd')

# Сложные фильтры https://docs.djangoproject.com/en/3.0/ref/models/querysets/
# 1. больше меньше (например найти все посты с рейтингом больше 3)
# Post.objects.filter(rating__gt=3)
# Post.objects.filter(rating__lt=3)
# Post.objects.filter(rating__lte=3)
# Post.objects.filter(rating__gte=3)
# 2. Посты с рейтингом 3 или 4
#  Post.objects.filter(rating__gte=3, rating__lte=4)
#  Post.objects.filter(rating__in=[3,4])
# 3. Посты начинающиеся (name) на ta...
# Post.objects.filter(name__startswith='ta')
# 4. Посты в имени которых есть nk, ...nk...
# Post.objects.filter(name__contains='nk')
# 5. Посты с датой создания меньше какой-то
#  import datetime
# >>> some_date = datetime.datetime(year=2000, month=1, day=1)
# >>> Post.objects.filter(create__gt=some_date)

# Post.objects.filter(create__year=2000, create__day=1, create__month=1)
# Post.objects.filter(create__year=2000, create__day=1, create__month__gt=1)
# Post.objects.filter(create__in=[some_date]) (можно добавить список из дат)

# 6. Запросы к связанным моделям
# Задача: 1. получить посты с категорией у которой имя cars
# Вариант "на python"
# >>> cars = Category.objects.get(name='cars')
# >>> Post.objects.filter(category=cars)
# Вариант "на orm"
# Post.objects.filter(category__name='cars')
# Goods.objects.filter(shop__city__country__president__wife__name='Kate')

# Задача: 2. получить посты с категорией у которой имя начинается на ca
# Post.objects.filter(category__name__startswith='ca')
