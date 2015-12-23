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
    trellogroup.add_argument('-t-cc', action="store_true", dest='trello_create_card_switch', default=False, help='Create new trello cards')
    trellogroup.add_argument('-t-dub', action="store_true", dest='trello_display_uboard_switch', default=False, help='Display boards belonging to user')
    trellogroup.add_argument('-t-dbl', action="store_true", dest='trello_display_board_list_switch', default=False, help='Display lists on a board')
    trellogroup.add_argument('-t-dlc', action="store_true", dest='trello_display_list_switch', default=False, help='Display cards on a list')
    trellogroup.add_argument('-t-gus', action="store_true", dest='trello_generate_user_stat_switch', default=False, help='Save broad user statistics to a CSV file')
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


    if results.trello_display_uboard_switch==True:
            username = raw_input('Provide your Trello username: ')
            trello_module.displayUserBoards(username, verbose=True)

    if results.trello_display_board_list_switch==True:
            boardid = raw_input('Provide the Trello board id: ')
            trello_module.displayBoardLists(boardid, verbose=True)

    if results.trello_display_list_switch==True:
            listid = raw_input('Provide Trello listid: ')
            trello_module.displayListCards(listid, verbose=True)

    if results.trello_generate_user_stat_switch==True:
            username = raw_input('Provide Trello username: ')
            trello_module.generateUserStats(username)

if __name__ == '__main__':
    pass
