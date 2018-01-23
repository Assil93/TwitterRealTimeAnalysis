
## Example to use twitter api and feed data into kinesis

from TwitterAPI import TwitterAPI
import boto3
import json
import TwitterCredentials




## twitter credentials

consumer_key = TwitterCredentials.consumer_key
consumer_secret = TwitterCredentials.consumer_secret
access_token_key = TwitterCredentials.access_token_key
access_token_secret = TwitterCredentials.access_token_secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis')

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})
tweets = []
count = 0

for item in r:
        jsonItem = json.dumps(item)
        tweets.append({'Data':jsonItem, 'PartitionKey':"filler"})
        count += 1
        
        if count == 500:
                if 'text' in item:
                        kinesis.put_records(StreamName="twitter-stream", Records=tweets)
                        count = 0
                        tweets = []
                        print (item['text'])
