from django.db import models

# Create your models here.
"""Cat_Choice=(
	(' ', 'Your choice'),
	('eng', 'English'),
	('quant', 'Quantitative'),
	('logic', 'Logical'),
	('tech', 'Technical'),
)

class Sample(models.Model):
	category = models.CharField(max_length=20, choices=Cat_Choice, default=' ')
"""

class Sample2(models.Model):
	name = models.CharField(max_length=20)
	dob = models.DateField()
	email = models.EmailField()
	class Meta:
		db_table="student"
