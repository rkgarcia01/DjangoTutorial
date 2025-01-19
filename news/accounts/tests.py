from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.


class SignupPageTests(TestCase):
    # Checks that our signup page is at the correct URL and returns a 200 status
    # code
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    # Checks the view.
    #  - It reverses signup which is the URL name, confirms a 200 status code, and
    #    that our 'signup.html' template is being used
    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    # Checks our form by sending a 'post' request to fill out
    #  - We expect a 302 redirect after the form is submitted and then confirm that
    #  - there is now one user in the test database with a matching 'username' and
    #  - 'emailaddress'

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")


"""
* By default, We do not check the password because Django automatically encrypts them
* That is why if you look in the admin view of a user, you can change a password 
*  But you cannot see what the current one actually is. 
"""
