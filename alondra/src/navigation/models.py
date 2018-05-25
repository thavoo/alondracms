# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from utilities.models import BaseDateTime
from utilities.models import BasePublish
from utilities.models import BaseSeo
from mptt.managers import TreeManager


class NavigationPosition(BaseDateTime,BasePublish):
    name = models.CharField(
            _('NAME_LABEL'),
            max_length=255,
            unique=True,
            blank=True      
        )

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _('NAVIGATION_POSITION_TITLE')
        verbose_name_plural = _('NAVIGATION_POSITION_TITLE_PLURAL')
        get_latest_by = 'created'
        ordering = ('-id',)
        db_table = 'navigation_position'
        app_label = 'navigation'



class NavigationItem(MPTTModel, BaseDateTime, BasePublish):

    position = models.ForeignKey(
            NavigationPosition,
            verbose_name=_('NAVIGATION_POSITION_TITLE'),
            null=True,
            blank=True,
            on_delete=models.CASCADE,
            related_name='navigation_item_position_parent'
        )

    parent = TreeForeignKey(
            'self',
            verbose_name=_('PARENT_LABEL'),
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='navigation_item_parent'
        )

    title = models.CharField(
            _('TITLE_LABEL'),
            max_length=255,
            unique=True,
            blank=True      
        )

    link = models.TextField(
            _('SLUG_LABEL'),
        )

    image = models.TextField(
            _('IMAGE_LABEL'),
        )


    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('NAVIGATION_ITEM_LABEL')
        verbose_name_plural = _('NAVIGATION_ITEM_PLURAL_LABEL')
        get_latest_by = 'created'
        ordering = ('-id',)
        db_table = 'navigation_item'
        app_label = 'navigation'

