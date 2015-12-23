"""
This is the Trello module that contains all methods related to
retrieval of data from the configured Trello account
"""
import argparse
import ConfigParser
from trello import TrelloApi
import os.path
import json
import pandas

def buildTrelloToken():
    if os.path.exists('config.cfg') == False:
        print "Error: Create a Trello config first with -tc"
        exit(1)

    config = ConfigParser.SafeConfigParser()
    config.read('config.cfg')
    if config.has_section('TRELLO CONFIGURATION'):
        if config.get('TRELLO CONFIGURATION', 'API_KEY') != "" and config.get('TRELLO CONFIGURATION', 'USER_HASH') != "" :
            trelloapikey = config.get('TRELLO CONFIGURATION', 'API_KEY')
            trellouserhash = config.get('TRELLO CONFIGURATION', 'USER_HASH')
            trello = TrelloApi(trelloapikey, token=trellouserhash)
            return trello
        else:
            print "Not all Trello access values present in config.cfg. Check your configuration file or run -tc option.\n"
            exit(1)


#List functions
def displayListCards(boardlistid, verbose):
    trello = buildTrelloToken()
    listcardids = trello.lists.get_card(boardlistid, fields=['id', 'name'])
    if verbose == True:
        print '\nYour list contains the following cards'
        for i in listcardids:
            print json.dumps(i)
    return listcardids

def displayBoardLists(boardid, verbose):
    trello = buildTrelloToken()
    listids = trello.boards.get_list(boardid, fields=['id', 'name'])
    if verbose == True:
        print '\nYour list contains the following cards'
        for i in listids:
            print json.dumps(i)
    return listids

def displayUserBoards(username, verbose):
    trello = buildTrelloToken()
    memberidraw = trello.members.get(username, fields='id')
    userid = str(json.dumps(memberidraw))[8:-2]
    userboards = trello.members.get_board(userid, fields=['id', 'name'])
    if verbose == True:
        print 'Trello id for user', username, 'is', userid
        print '\nYour are attached to the following Trello boards'
        for i in userboards:
            print json.dumps(i)
    return userboards

#Create functions
def createCards(number, boardlistid, cardpattern):
    trello = buildTrelloToken()
    for i in xrange(number):
        cardname = cardpattern + str(i)
        trello.lists.new_card(boardlistid, name=cardname)
        print 'added card', cardname


#Generate Trello statistics
def generateUserStats(username):
    verbose = False
    userboards = displayUserBoards(username, verbose)
    stats_file = username + '_statistics.csv'

    with open(stats_file, 'w') as filename:
        pd = pandas.DataFrame(userboards)
        pd.to_csv(stats_file)
            #wr.writerow(i)



if __name__ == '__main__':
    pass
