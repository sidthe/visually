"""
This module implements the menu for Visually
"""

import argparse
import sys
import integrate_service
import create_config

def visuallyMenu():
    visuallydescriptiontext = str('#'*70 + '\nVisually is a statistics app for Trello, Github, Bugzilla\n' + '#'*70)
    parser = argparse.ArgumentParser(description=visuallydescriptiontext)
    parser.add_argument('--make-config', action="store_true", dest='make_config_switch', default=False, help='Create Visually base configuration file')
    parser.add_argument('--trello-access', action="store_true", dest='trello_config_switch', default=False, help='Add Trello access parameters')

    results = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    if results.make_config_switch==True:
        create_config.createBaseConfig()

    if results.trello_config_switch==True:
        create_config.createTrelloConfig()
        print 'Added Trello parameters to the configuration file'

if __name__ == '__main__':
    pass
