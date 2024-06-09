from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def get_performer(self):
        if hasattr(self, 'performer'):
            return self.performer
        return None

    def get_customer(self):
        if hasattr(self, 'customer'):
            return self.customer
        return None
