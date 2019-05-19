import os
from lib.utils.config_generator import ConfigGenerator

# todo get arguments optionally via command line
testserver = os.path.abspath("storage/sample_configs/app-dev.json")
prodserver = os.path.abspath("storage/sample_configs/app-prod.json")
prod_config_yml = os.path.abspath("storage/sample_configs/production-config.yml")
    
try:
   c = ConfigGenerator(prod_config_yml, testserver, prodserver)
   c.create_prod_config()

except Exception as e:
     print(str(e))
     raise
     print("Aborted.")