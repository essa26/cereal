#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

from main.models import Manufacturer, Cereal, Nutritional_facts

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , "cereal.csv")

#csv_file_path2 = "%s/cereal.csv" % os.path.dirname(os.path.abspath(__file__))

#print os.path.abspath(__file__)

#print os.path.dirname(os.path.abspath(__file__))

#print csv_file_path

#print csv_file_path2

csv_file = open(csv_file_path, 'r')

#print csv_file

reader = csv.DictReader(csv_file)

#print reader

for row in reader:
    #for k, v in row.items():
        #print k
        #print v
    #print row['Cereal Name'].replace('_', ' ')#to remove underscores for spaces
    #print row['Manufacturer']

    #print row
    manu_obj, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])
    manu_obj.save()

    # print manu_obj.name
    # print created

    cereal_obj, created = Cereal.objects.get_or_create(name=row['Cereal Name'])#.replace('_', ' '))
    cereal_obj.type = row['Type']
    cereal_obj.manufacturer = manu_obj
    cereal_obj.save()

    nutri_obj, created = Nutritional_facts.objects.get_or_create(cereal=cereal_obj)
    nutri_obj.calories = row['Calories']
    nutri_obj.protein = row['Protein (g)']
    nutri_obj.fat = row['Fat']
    nutri_obj.sodium = row['Dietary Fiber']
    nutri_obj.carbs = row['Carbs']
    nutri_obj.fiber = row['Dietary Fiber']
    nutri_obj.sugars = row['Sugars']
    nutri_obj.display_shelf = row['Display Shelf']
    nutri_obj.potassium = row['Potassium']
    nutri_obj.vitamins_and_minerals = row['Vitamins and Minerals']
    try: 
        nutri_obj.save()
    except Exception, e:
        print e
        print row['Cereal Name']

    #nutri_obj, created = 


    # print row['Type']
    # print row['Calories']
    # print row['Protein (g)']
    # print row['Fat']
    # print row['Sodium']
    # print row['Dietary Fiber']
    # print row['Carbs']
    # print row['Sugars']
    # print row['Display Shelf']
    # print row['Potassium']
    # print row['Vitamins and Minerals']
    # print row['Serving Size Weight']
    # print row['Cups per Serving']


