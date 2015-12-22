"""
This is the Trello module that contains all methods related to
retrieval of data from the configured Trello account
"""
import argparse
import ConfigParser
from trello import TrelloApi

def createCards(number, boardlistid, cardpattern):
    for i in xrange(number):
        cardname = cardpattern + str(i)
        trello.lists.new_card(boardlistid, name=cardname)
        print 'added card', cardname
    print 'your list has following objects', (trello.lists.get_card(boardlistid, fields='id'))



#reads the config.cfg file
config = ConfigParser.SafeConfigParser()
config.read('config.cfg')
if config.has_section('TRELLO CONFIGURATION'):
    if config.has_option('TRELLO CONFIGURATION', 'API_KEY') and config.has_option('TRELLO CONFIGURATION', 'USER_HASH') :
        try:
            trelloapikey = config.get('TRELLO CONFIGURATION', 'API_KEY')
            trellouserhash = config.get('TRELLO CONFIGURATION', 'USER_HASH')

        except ValueError:
            print "Not all Trello access values present in config.cfg"


trello = TrelloApi(trelloapikey, token=trellouserhash)
print trello


if __name__ == '__main__':
    pass
