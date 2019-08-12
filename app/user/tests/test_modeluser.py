from django.test import TestCase
from django.contrib.auth import get_user_model

def sample_user(email='test@gmail.com', password='pass123', username='test'):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email"""
        email = 'test@gmail.com'
        password = 'pass123'
        username = 'test'
        user = get_user_model().objects.create_user(
			email=email,
			password=password,
            username=username,
		)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
