#mylist = ['apple', 'banana', 'monkey', 'love']
#
#s1="Monkeys love bananas"    
#print(len([each for each in mylist if each.lower() in s1.lower()])>=2)
#
#s2="The dog loves cats"
#print(len([each for each in mylist if each.lower() in s2.lower()])>=2)


# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "YOUR_API_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.search().list(
        part="snippet",
        q="tesseract ",
        safeSearch="strict"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()