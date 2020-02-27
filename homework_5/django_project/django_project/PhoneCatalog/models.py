from django.db import models


# Create your models here.
class PhoneCatalog(models.Model):
	"""Phone book model."""
	name = models.CharField(max_length=225)
	reg_date = models.DateTimeField()
	address = models.CharField(max_length=225)
	phone = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = 'Телефоны'
		verbose_name = 'Телефон'
