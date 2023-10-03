from django.contrib.auth.models import BaseUserManager


class ClientUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, birth_date, phone, city, address, password=None, **extra_fields):
        """
        creating and save default user
        """
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The Name field must be set')
        if not last_name:
            raise ValueError('The Surname field must be set')
        if not birth_date:
            raise ValueError('The Birthday field must be set')
        if not phone:
            raise ValueError('The Phone Number field must be set')
        if not city:
            raise ValueError('The City field must be set')
        if not address:
            raise ValueError('The Address field must be set')

        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, birth_date=birth_date, phone=phone,
                          city=city, address=address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, birth_date, phone, city, address, password=None, **extra_fields):
        """
        creating and save superuser
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(first_name, last_name, email, birth_date, phone, city, address, password, **extra_fields)
