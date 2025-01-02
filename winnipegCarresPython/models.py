from django.db import models

# Community Model
class Community(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# User Model (If using a custom user model)
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

# Volunteer Model
class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.TextField()
    available_from = models.DateField()
    available_to = models.DateField()

    def __str__(self):
        return f'{self.user.full_name} - {self.community.name}'

# Offer Model
class Offer(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    help_type = models.ForeignKey('HelpType', on_delete=models.CASCADE)
    help_category = models.ForeignKey('HelpCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
# Request Model
class Request(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    help_type = models.ForeignKey('HelpType', on_delete=models.CASCADE)
    help_category = models.ForeignKey('HelpCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# HelpType Model
class HelpType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

# HelpCategory Model
class HelpCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
