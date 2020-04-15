#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import requests


def basic_get_rate():
    API_TOKEN = os.getenv(key="API_TOKEN", default=None)
    url = "https://api.sandbox.transferwise.tech/v1/rates?source=EUR&target=USD"
    session = requests.Session()
    session.headers.update(
        {"Content-Type": "application/json", "Authorization": f"Bearer {API_TOKEN}"}
    )
    request = session.get(url=url)

    print(f"request json: {request.json()}")
    print(f"request dict: {request.__dict__}")

    return request


if __name__ == "__main__":
    basic_get_rate()
