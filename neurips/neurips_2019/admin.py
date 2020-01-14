from django.contrib import admin

# Register your models here.
from .models import Conference, Topic, Author, Institution, Authored_by, Url

admin.site.register(Conference)
admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Institution)
admin.site.register(Authored_by)
admin.site.register(Url)