# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['username']) < 3:
         # or not postData['username'].isalpha():
            errors["username"] = "Username should be at least three alphabetical characters."
        if len(User.objects.filter(username=postData['username'])) > 0:
            errors["existing_username"] = "Username is already in use. Please pick another username."
        if len(postData['password']) < 8:
            errors['password_length'] = 'Your password must be at least 8 characters.'
        if postData['password'] != postData['re_password']:
            error['password_match'] = 'Your passwords do not match.'
        return errors

class User(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User: {} {}>".format(self.id, self.username)

class HeroManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not postData['name'].isalpha():
            errors["name"] = "Please only use alphabetical characters in your adventurer's name."
        return errors

class Hero(models.Model):
    name = models.CharField(max_length = 255)
    health = models.PositiveIntegerField(default=150)
    player = models.ForeignKey('User', related_name='character')
    inventory = {}
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = HeroManager()
    def add_inventory(self, item, description):
        inventory['item'] = description
        return inventory
    def __repr__(self):
        return "<Hero: {} {} {}h>".format(self.id, self.name, self.health)

class LocationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        return errors

class Location(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    objects = {}
    ############# MAKE EXITS INTO DICTIONARY ############
    #########THIS IS RIDICULOUS WHY DID YOU DO THIS #####
    # exit_north = None
    # exit_south = None
    # exit_east = None
    # exit_west = None
    # exit_in = None
    # exit_out = None
    # exit_up = None
    # exit_down = None
    ############## nope not this either #################
    # def exits(self):
    #     all_exits = {}
    #     if exit_north:
    #         all_exits['north'] = self.exit_north
    #     if exit_south:
    #         all_exits['south'] = self.exit_south
    #     if exit_east:
    #         all_exits['east'] = self.exit_east
    #     if exit_west:
    #         all_exits['west'] = self.exit_west
    #     if exit_in:
    #         all_exits['in'] = self.exit_in
    #     if exit_out:
    #         all_exits['out'] = self.exit_out
    #     if exit_up:
    #         all_exits['up'] = self.exit_up
    #     if exit_down:
    #         all_exits['down'] = self.exit_down
    #     return all_exits
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = LocationManager()
    def __repr__(self):
        return "<Loc: {} {} - {}>".format(self.id, self.name, self.description)

class ItemManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        return errors

class Item(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    actions = [] ## look, get, get {} from, put {} in, eat?, sit
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ItemManager()
    def __repr__(self):
        return "<Item: {} {} - {}>".format(self.id, self.name, self.description)
