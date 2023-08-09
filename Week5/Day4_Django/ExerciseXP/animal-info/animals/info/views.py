from django.shortcuts import render
from django.http import HttpResponse
from .data import animals, families

# Create your views here.


def display_all_animals(request):
    animal_all = []
    for animal in animals:
        animal_all.append(
            f'Name - {animal["name"]}, Legs - {animal["legs"]}, Weight - {animal["weight"]}, Height - {animal["height"]}, Speed - {animal["speed"]}'
        )
    return HttpResponse(animal_all)


def display_all_families(request):
    family_name = []
    for family in families:
        family_name.append(f'{family["name"]}\n')
    return HttpResponse(family_name)


def display_one_animal(request, animal_id: int):
    for animal in animals:
        if animal["id"] == animal_id:
            return HttpResponse(
                f'Name - {animal["name"]}, Legs - {animal["legs"]}, Weight - {animal["weight"]}, Height - {animal["height"]}, Speed - {animal["speed"]}'
            )


def display_animal_per_family(request, family_id: int):
    for family in families:
        for animal in animals:
            if family_id == animal["family"]:
                return HttpResponse(
                    f'Family: {family["name"]} Pet: {animal["name"]}, {animal["legs"]}'
                )
