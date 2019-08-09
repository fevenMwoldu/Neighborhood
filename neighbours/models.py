from django.db import models


# Create your models here.

class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length = 30)
    neighbourhood_location = models.CharField(max_length =30)
    occupants_count = models.IntegerField()

    def __str__(self):
        return self.neighbourhood_location

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

class NeighbourhoodUser(models.Model):
    username = models.CharField(max_length = 30)
    user_id = models.IntegerField
    user_email = models.CharField(max_length = 30)
    neighbourhood = models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.username

    def save_neighbourhooduser(self):
        self.save()

    def delete_neighbourhooduser(self):
        self.delete()

class Bussiness(models.Model):
    bussiness_name = models.CharField(max_length = 30)
    bussiness_email = models.CharField(max_length = 30)
    neighbourhood = models.ForeignKey(Neighbourhood)
    neighbourhood_user = models.ForeignKey(NeighbourhoodUser)

    def __str__(self):
        return self.bussiness_name

    def save_bussiness(self):
        self.save()

    def delete_bussiness(self):
        self.delete()

    @classmethod
    def search_by_bussinessname(cls,search_term):
        bussinesses = cls.objects.filter(bussiness_name__icontains=search_term)
        return bussinesses

class Postcontent(models.Model):
    content = models.CharField(max_length = 800)
    neighbouhood_user = models.ForeignKey(NeighbourhoodUser)
   

    def __str__(self):
        return self.content

    def save_postcontent(self):
        self.save()

    def delete_postcontent(self):
        self.delete()

class Profile(models.Model):
    User_bio = models.CharField(max_length =300)
    neighbouhood = models.ForeignKey(Neighbourhood)
    neighbouhood_user = models.ForeignKey(NeighbourhoodUser)
   

    def __str__(self):
        return self.User_bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class NeighbourhoodLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

