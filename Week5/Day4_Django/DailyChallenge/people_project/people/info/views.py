from django.shortcuts import render
from django.http import HttpResponse

name = 'Bob Smith'
age = 35
country = 'USA'

people = ['bob','martha', 'fabio', 'john']

all_people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

# Create your views here.

def display_person(request):
    return HttpResponse(f'{name},{age},{country}')

def display_people(request):
    names = []
    for name in people:
        names.append(f'{name.capitalize()} ')
        
    return HttpResponse(sorted(names))

def display_all_people(request):
    newlist = sorted(all_people, key=lambda person: person['age']) 
    return HttpResponse(newlist)
    