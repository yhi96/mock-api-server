import json
import requests


with open('tests/config.json', 'r') as file:
    config = json.load(file)

use_https = config["use_https"]
cert_path = config["https_cert"] if use_https else None

url = "https://localhost:8080/" if use_https else "http://localhost:8080/"
verify = cert_path if use_https else True
