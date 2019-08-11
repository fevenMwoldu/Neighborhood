from django.test import TestCase
from .models import Neighbourhood,CustomUser,Bussiness,Post,User

# Create your tests here.


class NeighbourhoodTestClass(TestCase):

    # Set up method
    def setUp(self):
        user = User.objects.create(username='feven')
        self.yaya = Neighbourhood(name='yaya', location='kilimani', occupants_count=1000,admin=user)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.yaya, Neighbourhood))

    # Testing Save Method
    def test_save_method(self):
        self.yaya.save_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)

    # Testing delete method
    def tearDown(self):
        Neighbourhood.delete_neighbourhood


class CustomUserTestClass(TestCase):

    # Set up method
    def setUp(self):
        user = User.objects.create(username='feven')
        self.yaya = Neighbourhood(name='yaya', location='kilimani', occupants_count=1000, admin=user)
        self.yaya.save_neighbourhood()
        self.simon = CustomUser(first_name='simon', last_name='mebrahtu', bio='This is me simon from ...', profile_pic='/home/feven/Pictures/Moringa_pics', user=user, neighbourhood=self.yaya)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.simon, CustomUser))

    # Testing Save Method
    def test_save_method(self):
        self.simon.save_customuser()
        user_profiles = CustomUser.objects.all()
        self.assertTrue(len(user_profiles) > 0)

    # Testing delete method
    def tearDown(self):
        CustomUser.delete_customuser
        


class BussinessTestClass(TestCase):

    # Set up method
    def setUp(self):
        user = User.objects.create(username='feven')
        self.yaya = Neighbourhood(name='yaya', location='kilimani', occupants_count=1000, admin=user)
        self.yaya.save_neighbourhood()
        self.simon = CustomUser(first_name='simon', last_name='mebrahtu', bio='This is me simon from ...',profile_pic='/home/feven/Pictures/Moringa_pics', user=user, neighbourhood=self.yaya)
        self.simon.save_customuser()
        self.cafe = Bussiness(name='Artcafe', email='Artcafe@gmail.com', telephone=0-12345678, address="yaya center", category="bussiness", contact=self.simon, neighbourhood=self.yaya)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.cafe, Bussiness))

    # Testing Save Method
    def test_save_method(self):
        self.cafe.save_bussiness()
        bussinesses = Bussiness.objects.all()
        self.assertTrue(len(bussinesses) > 0)

    # Testing delete method
    def tearDown(self):
        Bussiness.delete_bussiness
        


class PostTestClass(TestCase):
        # Set up method
    def setUp(self):
        user = User.objects.create(username='feven')
        self.yaya = Neighbourhood(name='yaya', location='kilimani', occupants_count=1000, admin=user)
        self.yaya.save_neighbourhood()
        self.simon = CustomUser(first_name='simon', last_name='mebrahtu', bio='This is me simon from ...',profile_pic='/home/feven/Pictures/Moringa_pics', user=user, neighbourhood=self.yaya)
        self.simon.save_customuser()
        self.event = Post(title='New Library opening', content='There is a new library opening, everyone is invited', created_on='Aug. 11, 2019, 12: 24 a.m', created_by=self.simon, neighbourhood=self.yaya, post_pic='/home/feven/Pictures/Moringa_pics')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.event, Post))

    # Testing Save Method
    def test_save_method(self):
        self.event.save_post()
        events = Post.objects.all()
        self.assertTrue(len(events) > 0)

    # Testing delete method
    def tearDown(self):
        Post.delete_post
       
