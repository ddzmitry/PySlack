
from slackclient import SlackClient
import os
# Make your own
slack_token =   os.environ['TOKEN_SLACK']
# Set upt client
sc = SlackClient(slack_token)
# Call channels history
data = sc.api_call(
  "channels.history",
  channel='C8WJUBLGN',
  count = '1000'
)
# Get messages
messages = data.get('messages')
def GetData():
    needed_data = []
    # Get user Get mesage
    data_users = list(map(lambda x : x.get('user'),messages))
    # Make a count per user
    total_messages_result_dict = dict( [ (i, data_users.count(i)) for i in set(data_users) ] )
    for i in total_messages_result_dict:
        # Pull info for each user
        per_user_data = sc.api_call(
        "users.info",
        user= i,
        include_locale = True
        )
        # Build a partial API
        try:
            user_messager = dict(realname = per_user_data.get('user').get('real_name'),
                                slack_name = per_user_data.get('user').get('name'),
                                img_tag = per_user_data.get('user').get('profile').get('image_48'),
                                message_count = total_messages_result_dict[i]
                                )
            needed_data.append(user_messager)
        except AttributeError:
            print('Boo') 
    return needed_data