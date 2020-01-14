from django.db import models
import enum
import uuid

#TO DO: Add human-readable _self_ for each class
#TO DO: Experiment with Django admin https://docs.djangoproject.com/en/2.2/intro/tutorial02/
class Conference (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200) # Probably ought to expand this to capture country, city, state/province
    event_date = models.DateTimeField
    
    def __str__(self):
        return self.name
    
class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField #datetime
    conf_id = models.ForeignKey(Conference, on_delete=models.CASCADE)
    arxiv = models.CharField(max_length=200) # arxiv link, talk if arxiv = null
    poster = models.CharField(max_length=200) # Poster if poster != null
    video = models.CharField(max_length=200) #slidesLive link
    github = models.CharField(max_length=200) #github link
    slides = models.CharField(max_length=200) #S3 bucket link
    notes = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Author(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

#class Institution_type(enum.Enum):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#    APri = "Private Academic"
#    APub = "Public Academic"
#    IRes = "Industry Research"
#    IApp = "Industry Applied"

class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    INST_TYPE = (
        ('APri', 'Private Academic'),
        ('APub', 'Public Academic'),
        ('IRes', 'Industry Research'),
        ('IApp', 'Industry Applied')
    )

    inst_type = models.CharField(max_length=4, choices=INST_TYPE)

    def __str__(self):
        return self.name

class Authored_by(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    conf_id = models.ForeignKey(Conference, on_delete=models.CASCADE) 
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    author_id =models.ForeignKey(Author, on_delete=models.CASCADE)
    institution_id = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Url(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f'({self.topic_id.name}), {self.url}'