from django.db import models

from .Utils import CONSTANTS


# Create your models here.


class Contact(models.Model):
    contact_type = models.IntegerField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return CONSTANTS.GetName(self.contact_type)


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_descr = models.TextField()
    functionalities = models.TextField(default="")
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name + ", " + str(self.priority)


class Picture(models.Model):
    picture_file = models.ImageField(upload_to="./main_app/media")
    picture_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.picture_file.path


class Reference(models.Model):
    reference_url = models.CharField(max_length=300)
    reference_name = models.CharField(max_length=20)
    reference_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.reference_name + ": " + self.reference_project.project_name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    job_interest = models.CharField(max_length=200)
    birthday = models.DateField()
    biography = models.TextField()
    profile_pic = models.ImageField(upload_to="./main_app/media")

    def __str__(self):
        return self.name


class SocialSkill(models.Model):
    skill = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill


class File(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    file = models.FileField(upload_to="./main_app/files")

    def __str__(self):
        return self.label


class Download(models.Model):
    name = models.CharField(max_length=100)
    descr = models.TextField(default="")
    file = models.FileField(upload_to="./main_app/files")
    pic = models.ImageField(upload_to="./main_app/media", null=True)

    def __str__(self):
        return self.name


class Languages(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + str(self.priority)


class Frameworks(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + str(self.priority)


class OtherSkills(models.Model):
    name = models.CharField(max_length=150)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " - " + str(self.priority)


class SpokenLanguage(models.Model):
    language = models.CharField(max_length=150)
    level = models.CharField(max_length=150)

    def __str__(self):
        return self.language
