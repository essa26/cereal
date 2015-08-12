from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	name = models.CharField(max_length=30, unique=True)

	def __unicode__(self):
		return self.name

		
class Cereal(models.Model):
	name = models.CharField(max_length=30, unique=True)
	manufacturer = models.ForeignKey('main.Manufacturer', null=True)
	type = models.CharField(max_length=2, null=True)

	def __unicode__(self):
		return self.name

class Nutritional_facts(models.Model):
	calories = models.IntegerField(null=True)
	protein = models.IntegerField(null=True)
	fat = models.IntegerField(null=True)
	sodium = models.FloatField(null=True)
	fiber = models.FloatField(null=True)
	carbs = models.FloatField(null=True)
	sugars = models.IntegerField(null=True)
	display_shelf = models.IntegerField(null=True)
	potassium = models.IntegerField(null=True)
	vitamins_and_minerals = models.IntegerField(null=True) 
	cereal = models.OneToOneField('main.Cereal') #related_name="facts") related name reverse accessor for cereal
	
	def __unicode__(self):
		return self.cereal.name

	def nutrition_list(self):
		value_list = []
		value_list.append("Calories: %s cal" % self.calories) 
		value_list.append("Protein: %s g" % self.protein)
		value_list.append("Fat: %s " % self.fat)
		value_list.append("Sodium: %s " % self.sodium)
		value_list.append("Dietary Fiber: %s " % self.fiber)
		value_list.append("Carbs: %s " % self.carbs)
		value_list.append("Sugars: %s " % self.sugars)
		value_list.append("Display Shelf: %s " % self.display_shelf)
		value_list.append("Potassium: %s " % self.potassium )
		value_list.append("Vitamins and Minerals: %s " % self.vitamins_and_minerals)
		return value_list




	