# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Collection(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    poem_id = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection'


class Poem(models.Model):
    title = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poem'


class Review(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    poem_id = models.IntegerField(blank=True, null=True)
    poem_title = models.TextField(blank=True, null=True)
    poem_content = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class User(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    passwd = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
