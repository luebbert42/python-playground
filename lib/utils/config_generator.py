import json
import re
import os
import yaml
from pprint import pprint

class ConfigGenerator:
   
  def __init__(self, prod_config: str, test_json: str, prod_json: str):
    self.prod_config = prod_config
    self.test_json = test_json
    self.prod_json = prod_json

  def create_prod_config(self) -> None:
      prod_config_data = self.get_prod_config_data(self.prod_config, self.read_json(self.test_json))
      self.write_json(self.prod_json, prod_config_data)
      print("Prod config written to %s " % self.prod_json)

  def get_prod_config_data(self, prod_config: str, test_config_data: dict) -> dict:
          prod_config_data = test_config_data
          with open(prod_config, 'r') as ymlfile:
              to_insert = yaml.load(ymlfile, Loader=yaml.CLoader)
              # todo: loop through all items of to_insert -> remove hardcoded next line
              prod_config_data['properties']['templateFile'] = to_insert['properties']['templateFile']
          return prod_config_data

  def read_json(self, filename: str) -> dict:
          with open(filename) as json_file:  
              data = json.load(json_file)
              # pprint(locals())
              return data

  def write_json(self, filename: str, data: dict) -> None:
          with open(filename, 'w+') as json_file:  
                  dumped_json = json.dumps(data, indent=2, sort_keys=False, ensure_ascii=False, separators=(',', ': '))
                  tabbed_json = re.sub('\n +', lambda match: '\n' + '\t' * int((len(match.group().strip('\n')) / 2)), dumped_json)
                  json_file.write(tabbed_json)
                  json_file.close()
