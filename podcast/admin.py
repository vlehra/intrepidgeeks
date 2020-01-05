from django.contrib import admin

# Register your models here.
from .models import AudioFile,Writer,Episode
admin.site.register(Writer)
admin.site.register(Episode)
admin.site.register(AudioFile)