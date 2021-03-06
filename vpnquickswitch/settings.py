import os
import ConfigParser

class Settings(object):
    """
        Load configuration from file, or set defaults
    """
    options = {}

    def __init__(self):
        """
            Load configuration file
        """
        try:
            conf_loc = "/home/jjw/ini/vpnquickswitch"

            config = ConfigParser.ConfigParser()
            config.readfp(open(conf_loc))

            for item in config.options('vpnquickswitch'):
                self.options[item] = config.get('vpnquickswitch', item)

            return;

        except ConfigParser.ParsingError:
            print('ParsingError')
        except OSError as e:
            if isinstance(e, FileNotFoundError):
                print('Configuration not found')
                # make_file();
            else:
                raise e
        except Exception as e:
            print(e)

    def get_value(self, value):
        """
            Get config value, or if missing/incorrect, recreate
        """
        try:
            val = self.options.get(value)
            return val
        except Exception as e:
            print('Value missing')
            sys.exit()

    def make_file(self, file_loc):
        """
            TODO: Make Configuration file
        """
        pass


settings = Settings()
