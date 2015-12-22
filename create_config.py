"""
This module creates a configuration file if it does not exist
"""

import ConfigParser
import os.path
import integrate_service


def createBaseConfig():
    if os.path.exists('config.cfg') == False:
        config = ConfigParser.SafeConfigParser()

        config.add_section('TRELLO CONFIGURATION')
        config.set('TRELLO CONFIGURATION', 'API_KEY', '')
        config.set('TRELLO CONFIGURATION', 'USER_HASH', '')

        config.add_section('GITHUB CONFIGURATION')
        config.set('GITHUB CONFIGURATION', 'API_KEY', '')
        config.set('GITHUB CONFIGURATION', 'USER_HASH', '')

        with open('config.cfg', 'wb') as configfile:
            config.write(configfile)

        print 'No file exists. Created the configuration file config.cfg'

    else:
        print 'The configuration file already exists'


def createTrelloConfig():
    config = ConfigParser.SafeConfigParser()
    config.read('config.cfg')
    trelloapikey, trellouserhash = integrate_service.getTrelloCredentials()

    if config.has_section('TRELLO CONFIGURATION'):
        if config.has_option('TRELLO CONFIGURATION', 'API_KEY'):
            overwrite = raw_input('API_KEY option exists in config, overwrite? (y/n): ')
            if overwrite == 'y':
                config.set('TRELLO CONFIGURATION', 'API_KEY', trelloapikey)
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)


        if config.has_option('TRELLO CONFIGURATION', 'USER_HASH'):
            overwrite = raw_input('USER_HASH option exists in config, overwrite? (y/n): ')
            if overwrite == 'y':
                config.set('TRELLO CONFIGURATION', 'USER_HASH', trellouserhash)
        with open('config.cfg', 'w') as configfile:
            config.write(configfile)


    else:
        config.add_section('TRELLO CONFIGURATION')
        config.set('TRELLO CONFIGURATION', 'API_KEY', trelloapikey)
        config.set('TRELLO CONFIGURATION', 'USER_HASH', trellouserhash)

        with open('config.cfg', 'w') as configfile:
            config.write(configfile)



if __name__ == '__main__':
    pass
