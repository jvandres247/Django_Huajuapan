from django.db import models

from django.utils.safestring import mark_safe

# Create your models here.
class Twit(models.Model):
	text = models.CharField(max_length=280)
	image = models.ImageField('twits')

	def __str__(self):
		return self.text

	#defsave(self, *args, **kwargs):
		# Enviar twit
		# Add python-twitter
		# instance of python-twitter
		# send twit with self.text		
        #super(Twit, self).save(*args, **kwargs)
        #pass


	def thumb_image(self):
		return self.image.url


	def thumbnail(self):
		if self.image:
			return mark_safe(
				f'<image src="{self.image.url}" width=60 height=60 style="border-radius:50%" />'
				)
		else:
			return u'No image file found'

	thumbnail.short_description = 'Picture'
	thumbnail.allow_tags = True