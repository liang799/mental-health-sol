#import os
import discord
import re
import googleapiclient.discovery
import csv

#words = ['sad', 'melancholic', 'useless', 'retarded', 'anxiety', 'anxious', 'angry', 'mad', 'depressed', 'unhappy', 'down', 'dejected', 'despondent', 'downhearted', 'spiritless', 'pessimistic', 'bitter', 'heartbroken', 'sorrowful', 'distressed', 'grieve', 'troubled', 'mournful', 'somber', 'morbid']
client = discord.Client()
#TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
  print('\nDEBUGGING:')
  print('====================')
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #cleaning up the string
  lowerstring = message.content.lower()
  res = re.sub(' +', ' ', lowerstring)
  res = res.replace(',','')
  res = res.replace('.','')
  res = res.split()

  #storing contents of negative.txt into a list
  words = []
  file = open('negative.txt')
  for line in file:
    line = line.strip()
    words.append(line)

  #finding the keyword
  keyword = 'tmp'
  for word1 in res:
    for word2 in words:
      if word1 == word2:
        keyword = word2
  print('Keyword entered: ', keyword)

  query = keyword + ' music'
  print('Final Query: ', query)

  
  testdict = {
    "Mindfull1": "Hacks1"
    "Mindfull2" : "Hacks2"
    "Mindfull3" : "Hacks3"
  }





  # YOUTUBE-API
  # Disable OAuthlib's HTTPS verification when running locally.
  # *DO NOT* leave this option enabled in production.
  #os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

  #api_service_name = "youtube"
  #api_version = "v3"
  #DEVELOPER_KEY = "AIzaSyBFAz11pBz7EaZ6tskOXo8exDCIlBzTusc"
#
#  youtube = googleapiclient.discovery.build(
#      api_service_name, api_version, developerKey = DEVELOPER_KEY)
#
#  request = youtube.search().list(
#      part="snippet",
#      q=query,
#      safeSearch="strict"
#  )
#  response = request.execute()
#
#  #print(response)
#  try: 
#    with open('links.csv') as f:  
#      writer = csv.writer(f)
#      for k, v in response.items():
#        writer.writerow([k, v])
#  except IOError:
#    print("I/O error") 
#
  return

client.run('ODgzNjA0MjE4OTE1NzI1MzEy.YTMWjg.iU1SxH7dP4om7WkqPsp3V-W4mTg')