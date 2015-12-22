"""
This is the Trello module that contains all methods related to
retrieval of data from the configured Trello account
"""
import argparse
import ConfigParser
from trello import TrelloApi
import os.path
import json

def buildTrelloToken():
    if os.path.exists('config.cfg') == False:
        print "Error: Create a Trello config first with -tc"
        exit(1)

    config = ConfigParser.SafeConfigParser()
    config.read('config.cfg')
    if config.has_section('TRELLO CONFIGURATION'):
        if config.has_option('TRELLO CONFIGURATION', 'API_KEY') and config.has_option('TRELLO CONFIGURATION', 'USER_HASH') :
            trelloapikey = config.get('TRELLO CONFIGURATION', 'API_KEY')
            trellouserhash = config.get('TRELLO CONFIGURATION', 'USER_HASH')
            trello = TrelloApi(trelloapikey, token=trellouserhash)
            return trello
        else:
            print "Not all Trello access values present in config.cfg. Check your configuration file.\n"
            exit(1)



def createCards(number, boardlistid, cardpattern):
    trello = buildTrelloToken()
    for i in xrange(number):
        cardname = cardpattern + str(i)
        trello.lists.new_card(boardlistid, name=cardname)
        print 'added card', cardname


def displayListCards(boardlistid):
    trello = buildTrelloToken()
    listcardids = trello.lists.get_card(boardlistid, fields=['id', 'name'])
    print '\nYour list contains the following cards'
    for i in listcardids:
        print json.dumps(i)

def displayBoardLists(boardid):
    trello = buildTrelloToken()
    listids = trello.boards.get_list(boardid, fields=['id', 'name'])
    print '\nYour list contains the following cards'
    for i in listids:
        print json.dumps(i)

def displayUserBoards(username):
    trello = buildTrelloToken()
    memberidraw = trello.members.get(username, fields='id')
    userid = str(json.dumps(memberidraw))[8:-2]
    print 'Trello id for user', username, 'is', userid
    userboards = trello.members.get_board(userid, fields=['id', 'name'])
    print '\nYour are attached to the following Trello boards'
    for i in userboards:
        print json.dumps(i)



if __name__ == '__main__':
    pass
