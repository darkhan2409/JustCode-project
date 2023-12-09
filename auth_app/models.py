from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    SUPERADMIN, ADMINISTRATOR, CUSTOMER, SUPPLIER = range(1, 5)

    ROLE_GROUP = {
        SUPERADMIN: 1,
        ADMINISTRATOR: 2,
        CUSTOMER: 3,
        SUPPLIER: 4,
    }

    ROLE_TYPES = (
        (SUPERADMIN, 'SUPERADMIN'),
        (ADMINISTRATOR, 'ADMINISTRATOR'),
        (CUSTOMER, 'CUSTOMER'),
        (SUPPLIER, 'SUPPLIER'),
    )

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    bin = models.CharField(max_length=12, unique=True)
    role = models.IntegerField(ROLE_GROUP, choices=ROLE_TYPES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.username)
