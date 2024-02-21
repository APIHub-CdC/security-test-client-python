import unittest

from single_test import SingleTest


class Test(unittest.TestCase):

	def test_pruebas(self):
		x_api_key = "your_x_api_key"
		password = "your_keystore_password"
		pathKeypair = "/your_path/keypair.p12"
		pathCertificateCdc = "/your_path/cdc_cert.pem"
		basePath = "the_url"
		jsonRequest = '{"hola":"hola" }'
  
		single_test = SingleTest.prueba(self, x_api_key, password, pathKeypair, pathCertificateCdc, basePath, jsonRequest)
		self.assertTrue(single_test)
  

unittest.main()
