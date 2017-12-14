from django.db import models
from django.utils.text import slugify

		
class Features(models.Model):
	location = models.CharField(primary_key=True, db_column='LOCATION', unique=True, max_length=30)  # Field name made lowercase.
	class_field = models.CharField(db_column='CLASS', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
	latitude = models.TextField(db_column='LATITUDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
	longitude = models.TextField(db_column='LONGITUDE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
	map = models.CharField(db_column='MAP', max_length=30, blank=True, null=True)  # Field name made lowercase.
	elev = models.TextField(db_column='ELEV', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

	class Meta:
			managed = False
			db_table = 'FEATURES'

	def __str__(self):
		return self.location


class Flowers(models.Model):
	genus = models.CharField(db_column='GENUS', max_length=30, blank=True, null=True)  # Field name made lowercase.
	species = models.CharField(db_column='SPECIES', max_length=30, blank=True, null=True)  # Field name made lowercase.
	comname = models.CharField(primary_key=True, db_column='COMNAME', unique=True, max_length=30)  # Field name made lowercase.

	class Meta:
			managed = True
			db_table = 'FLOWERS'

	def get_image_name(self):
		path = 'media/flowers/'
		file = slugify(self.comname)
		return (path + file + ".jpg")

	def __str__(self):
		return self.comname

class Sightings(models.Model):
	name = models.CharField(db_column='NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
	person = models.CharField(db_column='PERSON', max_length=30, blank=True, null=True)  # Field name made lowercase.
	location = models.CharField(db_column='LOCATION', max_length=30, blank=True, null=True)  # Field name made lowercase.
	sighted = models.DateField(db_column='SIGHTED', blank=True, null=True)  # Field name made lowercase.

	class Meta:
			managed = True
			db_table = 'SIGHTINGS'
			unique_together = (('name', 'person', 'location', 'sighted'),)

