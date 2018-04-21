import factory
import factory.django

from .models import Human


class HumanFactory(factory.django.DjangoModelFactory):  

    class Meta:
        model = Human

    name = factory.Faker('name')
    phone = factory.Faker('phone_number')
    color = factory.Faker('safe_color_name')
