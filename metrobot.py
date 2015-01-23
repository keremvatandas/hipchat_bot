import random
import hipchat
"""
HipChat MiniBot
"""

API_KEY = 'xxxxxx'
ROOM_ID = 'xxxxxxx'
BOT_NAME = 'METROBOT'

photos = [
    'fullurl.jpg',
]

messages = [
    'messages',
]

emoticons = [
    'awyeah', 'boom', 'beer', 'ceilingcat', 'chompy', 'dance',
    'dealwithit', 'doge', 'fonzie', 'freddie', 'gangnamstyle',
    'gtfo', 'hipster', 'mindblown', 'orly', 'samuel',
    'shrug', 'success', 'yodawg', 'zoidberg'
]

base_params = {
    'room_id': ROOM_ID, 'message_from': BOT_NAME,
    'message_format': 'text', 'notify': 1, 'color': 'red'
}

hipster = hipchat.HipChat(token=API_KEY)
hipster.message_room(message='{0} ({1})'.format(
    random.choice(messages), random.choice(emoticons)), **base_params)
hipster.message_room(message=random.choice(photos), **base_params)
