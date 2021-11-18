import json
import logging
import os
import time

import requests

from key_handler import KeyHandler

global logger

class SingleTest:


    def prueba(self, x_api_key, password, pathKeypair, pathCertificateCdc, url, jsonRequest):
        global logger
        validate = False
        start_time = time.time()
        logging.basicConfig(level=logging.NOTSET)
        self.logger = logging.getLogger('SingleTest')
        key_handler = KeyHandler(pathKeypair,pathCertificateCdc,password)
        headers = {"Content-Type": "application/json","x-api-key": x_api_key,"x-signature": None}
        json_text = jsonRequest
        url_services = url
        self.logger.info("REQUEST ----> "+json_text)
        headers['x-signature'] = key_handler.get_signature_from_private_key(json_text)
        r = requests.post(url=url_services, data=json_text, headers=headers)
        r.encoding = 'utf-8'
        
        status_code = str(r.status_code)
        try:
            self.logger.info("RESPONSE ---->"+r.text)
            self.logger.info(key_handler.get_verification_from_public_key(r.text, r.headers['x-signature']))
            validate = key_handler.get_verification_from_public_key(r.text, r.headers['x-signature'])
        except Exception as e:
            json_resp = ""
            self.logger.error(e)
            validate = False
        self.logger.info("Total %s seconds execution" % (time.time() - start_time))
        return validate
    