from django.db import models

# Create your models here.


class Award(models.Model):
	award_id = models.IntegerField(primary_key=True) 
	first_selection = models.IntegerField(default=1)
	is_done= models.BooleanField(default=False)
	award_name =models.CharField(max_length=20,blank=True)
	descript_text = models.CharField(max_length=50,blank=True)
	award_content = models.CharField(max_length=50,blank=True)
	award_group_id = models.IntegerField(default=1)
	award_amount = models.IntegerField(default=1)

class Person(models.Model):
	person_id = models.IntegerField(primary_key=True,default=0)
	employee_id = models.CharField(max_length=40,default="",blank=True)
	company = models.CharField(max_length=20,default="",blank=True)
	name = models.CharField(max_length=20)
	department = models.CharField(max_length=50,default="",blank=True)
	seniority = models.IntegerField(default=1)
	is_attend =models.BooleanField(default=True)
	award = models.ManyToManyField(Award,blank=True)
	#create_date = models.DateTimeField('date created')
	def __str__(self):
		return self.name
