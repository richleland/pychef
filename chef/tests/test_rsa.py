import os

import unittest2

from chef.rsa import Key, SSLError
from chef.tests import TEST_ROOT

class RSATestCase(unittest2.TestCase):
    def test_load_private(self):
        key = Key(os.path.join(TEST_ROOT, 'client.pem'))
        self.assertFalse(key.public)

    def test_load_public(self):
        key = Key(os.path.join(TEST_ROOT, 'client_pub.pem'))
        self.assertTrue(key.public)

    def test_private_export(self):
        key = Key(os.path.join(TEST_ROOT, 'client.pem'))
        raw = open(os.path.join(TEST_ROOT, 'client.pem'), 'rb').read()
        self.assertTrue(key.private_export().strip(), raw.strip())

    def test_public_export(self):
        key = Key(os.path.join(TEST_ROOT, 'client.pem'))
        raw = open(os.path.join(TEST_ROOT, 'client_pub.pem'), 'rb').read()
        self.assertTrue(key.public_export().strip(), raw.strip())

    def test_private_export_pubkey(self):
        key = Key(os.path.join(TEST_ROOT, 'client_pub.pem'))
        with self.assertRaises(SSLError):
            key.private_export()

    def test_public_export_pubkey(self):
        key = Key(os.path.join(TEST_ROOT, 'client_pub.pem'))
        raw = open(os.path.join(TEST_ROOT, 'client_pub.pem'), 'rb').read()
        self.assertTrue(key.public_export().strip(), raw.strip())
