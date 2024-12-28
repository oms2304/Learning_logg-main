from django.contrib import admin
from learning_logs.models import Topic  #imports model we want to register
from learning_logs.models import Entry





admin.site.register(Topic) #tells Django to manage model (Topic) through admin site
admin.site.register(Entry) #tells Django to manage model (Entry) through admin site
