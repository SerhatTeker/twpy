# -*- coding: utf-8 -*-
""" Main module. """
import requests


class Client():
    BASE_URL_LIVE = "https://api.transferwise.com"
    BASE_URL_SANDBOX = "https://api.sandbox.transferwise.tech"
    API_VERSION = "v1"
    PROFILE = "profiles"
    RATES_PATH = "rates?source={}&target={}"
    QUOTE = "quotes"
    LIST_RECIPIENTS = "accounts?profile={}&currency={}"
    TRANSFERS = "transfers"
    CANCEL_TRANSFER = "transfers/{}/cancel"

    def __init__(self, api_token=None, requests_params=None):
        """TransferWise API Client constructor
        :param api_key: TransferWise Api Key
        :type api_key: str.
        :param requests_params: optional - Dictionary of requests params to use for all calls
        :type requests_params: dict.
        """

        self.BASE_API_URL = self.BASE_URL_SANDBOX + "/" + self.API_VERSION + "/"
        self.API_URL = None

        self.API_TOKEN = api_token
        self.session = self._init_session()
        self._requests_params = requests_params
        self.response = None

    def _init_session(self):
        session = requests.Session()
        session.headers.update(
            {"Accept": "application/json", "Authorization": f"Bearer {self.API_TOKEN}"}
        )

        return session
