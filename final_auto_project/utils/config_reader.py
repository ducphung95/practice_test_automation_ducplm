import json
import os
import datetime

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'testsetting.json')
            with open(config_path, 'r') as config_file:
                ConfigReader._config = json.load(config_file)
        return ConfigReader._config
    
    @staticmethod
    def get_base_url():
        return ConfigReader.load_config()['base_url']
    
    @staticmethod
    def get_username():
        return ConfigReader.load_config()['credentials']['username']
    
    @staticmethod
    def get_password():
        return ConfigReader.load_config()['credentials']['password']
    
    @staticmethod
    def get_timeout():
        timeout_settings = ConfigReader.load_config().get('timeout', {})
        return float(timeout_settings.get('implicit', 10))
    
    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    @staticmethod
    def load_config_path():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))