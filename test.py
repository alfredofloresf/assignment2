import unittest
import requests
from app import app

server_address = "http://127.0.0.1:5000"
SERVICE_ADDR = server_address


class FeatureTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.testing = True

    def test_server_is_alive(self):
        req = requests.get(server_address + "/register")
        self.assetrEqual(req.status_code, 200)
        print("OK")

    def test_login(self):
        req = requests.get(server_address + "/login")
        self.assertEqual(req.status_code, 200)
        print("OK")

if __name__ == '__main__':
    unittest.main()
