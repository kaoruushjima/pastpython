from django.test import TestCase
from django.contrib.auth.models import User

from bitly.models.bitlink import Bitlink


class BitlinkModelTestCase(TestCase):

    def test_bitlink_should_have_shorten_hash(self):
        # Create Test User
        test_username = "test_username"
        test_password = "test_password"
        test_user = User.objects.create_user(
            username=test_username,
            password=test_password,
        )

        # Create Test Bitlink
        test_original_url = "http://www.daum.net"
        bitlink = Bitlink.objects.create(
            user=test_user,
            original_url=test_original_url,
        )

        self.assertTrue(
            bitlink.shorten_hash,
        )
