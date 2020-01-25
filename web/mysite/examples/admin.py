from django.contrib import admin

from .models import Dog, Owner

admin.site.register(Owner)
admin.site.register(Dog)