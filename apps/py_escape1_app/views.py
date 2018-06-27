# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from .models import *

# Create your views here.
def index(request): ##login stuff
    context = {
        ## blah copy login stuff here
        ## might need a character select page/popup
    }
    return render(request, 'test_game_app/index.html', context)

def game(request): ##actual game, current code assuming character has been created
    request.session['activity_log'] = [] ## maybe have it pull up the starting location info
    context = {
        'current_location' : Location.objects.first(),
        'character' : Hero.objects.get(id=request.session['hero_id']),
        'inventory' :  Hero.objects.get(id=request.session['hero_id']).inventory.all(),
    }
    return render(request, 'test_game_app/game.html', context)

def look(request, item_id):
    if Item.objects.get(id = item_id).actions.find("look"):
        request.session['activity_log'].append("You look at " + Item.objects.get(id = item_id).name + ".\n")
        request.session['activity_log'].append(Item.objects.get(id = item_id).description)
    else:
        request.session['activity_log'].append("You can't look at" + item.name + ".") ## impossible but w/e
    return redirect(reverse('game'))

def get(request, item_id):
    if Item.objects.get(id = item_id).actions.find("get"):
        item = Item.objects.get(id = item_id)
        item.location_id = -1
        Hero.objects.get(id=request.session['hero_id']).inventory[item.name] = item
        request.session['activity_log'].append("You picked up " + item.name + ".")
    else:
        request.session['activity_log'].append("You can't pick " + item.name + " up.")
    return redirect(reverse('game'))

def move(request, location_id, direction): ## ?? location id should be in current_location
    current_location = Location.objects.get(id = location_id)
    ## do i need a method for each direction or can i supply it from input ##
    ### basically current_location = Location.objects.get(id = location_id).{{direction}}
    ###### IF CHECK MAKE SURE THERE'S A ROOM THERE if not null something
    return redirect(reverse('game'))

# def fight(request):
#     ## might not include this after all
#     return redirect(reverse('game'))

def admin(request):
    context = {
        'all_users' : User.objects.all(),
        'all_heroes' : Hero.objects.all(),
        'all_locations' : Location.objects.all(),
    }
    return render(request, 'test_game_app/admin.html', context)


################ how to make log clear oldest logs ##############
