# -*- coding: utf-8 -*-
from pprint import pprint

import yaml

from test_request.api.base_api import BaseApi


def test_load():
    with open("test_tag_data.yaml",'r') as f:
        pprint(yaml.safe_load(f))


def test_template():
    print(BaseApi.template("../api/test_add.yaml", {"token": '123', 'tag_name': 'daemo'}))