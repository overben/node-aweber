import sys
from aweber_api import AWeberAPI, APIException

email           = str(sys.argv[1])
validation_code = str(sys.argv[2])

#Your Credentials
consumer_key    =  'cred'
consumer_secret =  'en'
access_key      =  'ti'
access_secret   =  'als'

#list_id of the list you want to subscribe the user
list_id         =  'yourlistid'
aweber          = AWeberAPI(consumer_key, consumer_secret)

try:
    account = aweber.get_account(access_key, access_secret)
    list_url = '/accounts/%s/lists/%s' % (account.id, list_id)
    list_ = account.load_from_url(list_url)

    # create a subscriber
    params = {
        'email': email,
        'ad_tracking': validation_code,
    }

    subscribers = list_.subscribers
    new_subscriber = subscribers.create(**params)

except APIException, exc:
    print exc