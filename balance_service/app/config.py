# -*- coding: utf-8 -*-
"""Application configuration."""
import os
import logging


class config(object):
    """Base configuration."""
    # SWAGGER
    SWAGGER_URL = os.getenv('SWAGGER_URL', '/docs')
    SWAGGER_FILE_PATH = os.getenv(
        'SWAGGER_FILE_PATH', '/../../../swagger.yml')
    # APPLICATION
    APP_NAME = os.getenv('APP_NAME', 'Balance Service App')
    PORT = int(os.getenv('PORT', '5002'))
    BALANCE_NAMESPACE = os.getenv('BALANCE_NAMESPACE', 'account_balances')
    ENV = os.getenv('ENV', 'development')


class test_config():
    """Testing configuration."""
    TESTING = 'true'
    ENV = 'testing'
    # SWAGGER
    SWAGGER_URL = os.getenv('SWAGGER_URL', '/docs')
    SWAGGER_FILE_PATH = os.getenv(
        'SWAGGER_FILE_PATH', '/../../../swagger.yml')

    @classmethod
    def init_app(cls, app):
        logging.info('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')
