from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    image= models.TextField(verbose_name='Image')
    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    country = models.CharField(max_length=100, verbose_name='Country')
    address = models.CharField(max_length=100, verbose_name='Address')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    image = models.TextField(verbose_name='Image')
    category = models.ForeignKey(Category, verbose_name='Category')
    producer = models.ForeignKey(Producer, verbose_name='Producer')
    views = models.IntegerField(verbose_name='Views')
    price = models.FloatField(verbose_name='Price')
    count = models.IntegerField(verbose_name='Count')

    def __str__(self):
        return self.name


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    text = models.TextField(max_length=100, verbose_name='Text')
    user = models.ForeignKey('auth.User', verbose_name='Author')
    date = models.DateTimeField(default=timezone.now, verbose_name='Date')

    def __str__(self):
        return self.name


class Deal(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Client')
    date = models.DateTimeField(default=timezone.now, verbose_name='Date')
    checked = models.BooleanField(default=False, verbose_name='Is Checked')
    check_date = models.DateTimeField(default=timezone.now, verbose_name='Check date', null=True)
    status = models.CharField(max_length=100, verbose_name='Status')
    product = models.ForeignKey(Product, verbose_name='Product', null=True)
    adress = models.CharField(default='',max_length=100, verbose_name='Adress')
    telephone = models.CharField(max_length=100, verbose_name='Telephone')

    def __str__(self):
        return '%s - %s' % (self.user.__str__(), self.date)
