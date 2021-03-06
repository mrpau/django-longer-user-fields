from django.contrib.auth.models import User
from django.test import TestCase


class LongerUserFieldsTests(TestCase):
    """
    Unit tests for longeruserfields app.
    """

    def setUp(self):
        """
        Creates a user with a terribly long username
        """
        long_username = ''.join([str(i) for i in range(100)])
        self.user = User.objects.create_user('test' + long_username, 'test@test.com', 'testpassword')

    def testUserCreation(self):
        """
        Tests that self.user was successfully saved, and can be retrieved
        """
        self.assertNotEqual(self.user, None)
        User.objects.get(id=self.user.id) # returns DoesNotExist error if the user wasn't created
