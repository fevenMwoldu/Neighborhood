from django.db import models
import datetime as dt
from django.contrib.auth.models import User


# Create your models here.

class Neighbourhood(models.Model):
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length =30)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User)

    def __str__(self):
        return 'Neighbourhood (name: {self.name}, location: {self.location}, occupants_count: {self.occupants_count}, admin: {self.admin})'.format(self=self)

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

class CustomUser(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return 'CustomUser (first_name: {self.first_name}, last_name: {self.last_name}, bio: {self.bio}, profile_pic: {self.profile_pic}, user: {self.user}, neighbourhood: {self.neighbourhood} )'.format(self=self)

    def save_customuser(self):
        self.save()

    def delete_customuser(self):
        self.delete()

    def fullname(self):
        return '{self.last_name}, {self.first_name}'.format(self=self)

    @classmethod
    def user_has_profile(cls, user_id):
        profiles = CustomUser.objects.filter(user_id=user_id)
        return len(profiles) > 0

class Bussiness(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    telephone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    contact = models.ForeignKey(CustomUser)
    neighbourhood = models.ForeignKey(Neighbourhood)
   

    def __str__(self):
        return 'Business (name: {self.name}, email: {self.email}, telephone: {self.telephone}, address: {self.address}, category: {self.category}, contact: {self.contact}, neighbourhood: {self.neighbourhood})'.format(self=self)

    def save_bussiness(self):
        self.save()

    def delete_bussiness(self):
        self.delete()

    @classmethod
    def search_by_name(cls,search_term):
        bussinesses = cls.objects.filter(name__icontains=search_term)
        return bussinesses

    @classmethod
    def search_by_category(cls, search_term):
        bussinesses = cls.objects.filter(name__icontains=search_term)
        return bussinesses

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length = 800)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser)
    neighbourhood = models.ForeignKey(Neighbourhood)
    post_pic = models.ImageField(upload_to='photos/')

    def __str__(self):
        return 'Post (title: {self.title}, content: {self.content}, created_on: {self.created_on}, created_by: {self.created_by}, neighbourhood: {self.neighbourhood})'.format(self=self)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

