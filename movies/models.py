from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Genre(models.Model):
	g_name = models.CharField(max_length=30)

	def __str__(self):
		return self.g_name

class Movie(models.Model):
#	m_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=250)
	release_date = models.DateField(max_length=30)
	language = models.CharField(max_length=15)
#	genre = models.ForeignKey(Genre,  on_delete=models.CASCADE)
	genre = models.ManyToManyField(Genre)

	def __str__(self):
		return '%s (%s)' % (self.title,self.release_date.year)

class Tag(models.Model):
	t_name = models.CharField(max_length=15, unique=True)

	def __str__(self):
		return self.t_name

class Movie_Has_Tag(models.Model):
	m_id = models.ManyToManyField(Movie)	
	t_id = models.ManyToManyField(Tag)

class Crew(models.Model):
	crew_first_name = models.CharField(max_length=15)
	crew_last_name = models.CharField(max_length=15)
	role = models.CharField(max_length=15)

	m_id = models.ManyToManyField(Movie)

	def __str__(self):
		return u'%s %s' % (self.crew_first_name, self.crew_last_name)

class User(models.Model):
	GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
	('O', 'Other'),
	)
	first_name = models.CharField(max_length=15)
	middle_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	email = models.CharField(max_length=30,null=True)
	password = models.CharField(max_length=20,null=True)
	date_of_birth = models.DateField()
	manager = models.BooleanField(default=False)
	sex = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	
	def __str__(self):
		return u'%s %s' % (self.first_name, self.last_name)

class Review(models.Model):
	description = models.CharField(max_length=200)
	rating = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
	m_id = models.ManyToManyField(Movie)
	u_id = models.ManyToManyField(User)
	
	def __str__(self):
		return self.description
