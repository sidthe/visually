"""
This module implements the menu for Visually
"""

import argparse
import sys
import integrate_service
import create_config
import trello_module

def visuallyMenu():

    visuallydescriptiontext = str('#'*70 + '\nVisually is a statistics app for Trello, Github, Bugzilla\n' + '#'*70)
    parser = argparse.ArgumentParser(description=visuallydescriptiontext)

    configfilegroup = parser.add_argument_group('Configuration File', 'This argumens allow you to create and update the configuration file')
    configfilegroup.add_argument('-mc', action="store_true", dest='make_config_switch', default=False, help='Create default configuration file')
    configfilegroup.add_argument('-tc', action="store_true", dest='trello_config_switch', default=False, help='Add Trello access parameters to configuration file')

    trellogroup = parser.add_argument_group('Trello Control', 'This argumens allow you to manually operate Trello')
    trellogroup.add_argument('-t-cc', action="store_true", dest='trello_create_card_switch', default=False, help='Manually create new trello cards')
    trellogroup.add_argument('-t-dl', action="store_true", dest='trello_display_list_switch', default=False, help='Manually display cards on a list')

    results = parser.parse_args()

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)


    if results.make_config_switch==True:
        create_config.createBaseConfig()

    if results.trello_config_switch==True:
        create_config.createTrelloConfig()
        print 'Added Trello parameters to the configuration file'

    if results.trello_create_card_switch==True:
            listid = raw_input('Provide Trello listid: ')
            nrofcard = int(raw_input('Number of cards to create: '))
            namepattern = raw_input('Provide name pattern (ex:mycard): ')
            trello_module.createCards(nrofcard, listid, namepattern)

    if results.trello_display_list_switch==True:
            listid = raw_input('Provide Trello listid: ')
            trello_module.displayList(listid)

if __name__ == '__main__':
    pass
