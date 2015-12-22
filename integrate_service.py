"""
The service_integration module contain wizards that allow users
to retrieve credentials to access the APIs of the relevant platforms
"""


from trello import TrelloApi

"""this method walks the user through retrieving his trello access credentials,
such as the Trello API key and the user token"""
def getTrelloCredentials():
        print '\n', '#'*80, '\nAccess your Trello Developer API Key at https://trello.com/app-key\n', '#'*80, '\n'
        trelloapikey = str(raw_input('Paste your Developer API Key here: '))
        trellokey = TrelloApi(trelloapikey)

        visuallyaccesslink = trellokey.get_token_url('Visually', expires='30days', write_access=True)
        print '\n', '#'*80, '\nGive Visually 30 days write access to your Trello account by clicking on the following link: \n',  visuallyaccesslink, '\n', '#'*80, '\n'
        trellouserhash = str(raw_input('Paste your User Hash here: '))

        trellotoken = TrelloApi(trelloapikey, trellouserhash)

        return trelloapikey, trellouserhash


if __name__ == '__main__':
    getTrelloCredentials()
