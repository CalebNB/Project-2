
#Author - Caleb Burke 10/02/20

#This python script will search tweets from today posted on twitter
#that have people tweeting negative comments about flying
#at the end a report will be created

import os
import tweepy as tw
import pandas as pd
import csv
import time
import json
from openpyxl import Workbook

#first we will read in the twitter API keys from a txt file called twdev_keys
#it must be in the same directory.  We read in each line at a time and
#then save to variables first-fourth.  After that we associalte each line with a
#variable name that twitter API is looking for.

###########################################################
#read first line in the key file named twdev_keys.txt 
line_no = 1  
curr_line_no = 1 
with open('twdev_keys.txt','r') as f: 
    for rec in f: 
        if curr_line_no == line_no: 
            #saving that line into a variable called first 
            first = rec
            first = first.rstrip()
            #print(first) 
            break 
        else: 
            curr_line_no += 1
            
#read 2nd line in the key file named twdev_keys.txt
line_no = 2  
curr_line_no = 1 
with open('twdev_keys.txt','r') as f: 
    for rec in f: 
        if curr_line_no == line_no: 
            #saving that line into a variable called second 
            second = rec
            second = second.rstrip()
            #print(second) 
            break 
        else: 
            curr_line_no += 1
            
#read 3rd line in the file 
line_no = 3  
curr_line_no = 1 
with open('twdev_keys.txt','r') as f: 
    for rec in f: 
        if curr_line_no == line_no: 
            #saving that line into a variable called third 
            third = rec
            third = third.rstrip()
            #print(third) 
            break 
        else: 
            curr_line_no += 1 
     
#read 4th line in the file 
line_no = 4  
curr_line_no = 1 
with open('twdev_keys.txt','r') as f: 
    for rec in f: 
        if curr_line_no == line_no: 
            #saving that line into a variable called fourth 
            fourth = rec
            fourth = fourth.rstrip()
            #print(fourth) 
            break 
        else: 
            curr_line_no += 1
#############################################################################
            
#Twitter API credentials
consumer_key = first
consumer_secret = second
access_key = third
access_secret = fourth        
        
#authorize twitter, initialize tweepy
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tw.API(auth, wait_on_rate_limit=True)
    

search_words = "bad flight OR flight:(-filter:retweets"
date_since = "2020-10-02"



tweets = tw.Cursor(api.search, 
                           q=search_words,
                           lang="en",
                           since=date_since).items(10)

users_data = [[tweet.user.screen_name, tweet.text] for tweet in tweets]
users_data
#print(users_data)

#create a pandas Dataframe
name_tweet = pd.DataFrame(data=users_data, 
                    columns=['User', "Tweet"])

#print the dataframe for debugging
print(name_tweet)

#now save the data frame to an excel spread sheet
name_tweet.to_excel('tweets.xlsx', sheet_name='sheet_1')

# now read the data out of excel into variables to use
import openpyxl
workbook_read = openpyxl.load_workbook(r'tweets.xlsx')
sheet = workbook_read.active
u1 = sheet['B2'].value
u1t = sheet['C2'].value
u2 = sheet['B3'].value
u2t = sheet['C3'].value
u3 = sheet['B4'].value
u3t = sheet['C4'].value
u4 = sheet['B5'].value
u4t = sheet['C5'].value
u5 = sheet['B6'].value
u5t = sheet['C6'].value
u6 = sheet['B7'].value
u6t = sheet['C7'].value
u7 = sheet['B8'].value
u7t = sheet['C8'].value
u8 = sheet['B9'].value
u8t = sheet['C9'].value
u9 = sheet['B10'].value
u9t = sheet['C10'].value
u10 = sheet['B11'].value
u10t = sheet['C11'].value

#now save each tweet to its own spread sheet to feed into Google cloud language analyzer
#print(u1t)

tweet_text1 = [u1t]

with open('tweets/u1_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text1)

tweet_text2 = [u2t]

with open('tweets/u2_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text2)

tweet_text3 = [u3t]

with open('tweets/u3_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text3)

tweet_text4 = [u4t]

with open('tweets/u4_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text4)

tweet_text5 = [u5t]

with open('tweets/u5_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text5)


tweet_text6 = [u6t]

with open('tweets/u6_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text6)

tweet_text7 = [u7t]

with open('tweets/u7_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text7)

tweet_text8 = [u8t]

with open('tweets/u8_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text8)

tweet_text9 = [u9t]

with open('tweets/u9_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text9)

tweet_text10 = [u10t]

with open('tweets/u10_tweet.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    csv_writer.writerow(tweet_text10)
    
print("Now we will wait 3 seconds to make sure the system has time to create the files to analyze")
time.sleep(3)
print("Now analyzing individual tweets...This could take a minute or two")

#now take 10 tweets and use shell to send them through the Google NLP and store results in same folder
myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u1_tweet.csv > tweets/u1_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u2_tweet.csv > tweets/u2_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u3_tweet.csv > tweets/u3_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u4_tweet.csv > tweets/u4_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u5_tweet.csv > tweets/u5_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u6_tweet.csv > tweets/u6_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u7_tweet.csv > tweets/u7_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u8_tweet.csv > tweets/u8_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u9_tweet.csv > tweets/u9_sentiment_output.json'
os.system(myCmd)

myCmd = 'gcloud ml language analyze-sentiment --content-file=tweets/u10_tweet.csv > tweets/u10_sentiment_output.json'
os.system(myCmd)


import json
#open sentiment file and pull out the document sentiment magnitude and score
with open('tweets/u1_sentiment_output.json') as json_file:
    data1 = json.load(json_file)
#save the data for use later
u1sm = (data1['documentSentiment']['magnitude']) 
u1ss = (data1['documentSentiment']['score'])

with open('tweets/u2_sentiment_output.json') as json_file:
    data2 = json.load(json_file)
u2sm = (data2['documentSentiment']['magnitude']) 
u2ss = (data2['documentSentiment']['score'])

with open('tweets/u3_sentiment_output.json') as json_file:
    data3 = json.load(json_file)
u3sm = (data3['documentSentiment']['magnitude']) 
u3ss = (data3['documentSentiment']['score'])

with open('tweets/u4_sentiment_output.json') as json_file:
    data4 = json.load(json_file)
u4sm = (data4['documentSentiment']['magnitude']) 
u4ss = (data4['documentSentiment']['score'])

with open('tweets/u5_sentiment_output.json') as json_file:
    data5 = json.load(json_file)
u5sm = (data5['documentSentiment']['magnitude']) 
u5ss = (data5['documentSentiment']['score'])

with open('tweets/u6_sentiment_output.json') as json_file:
    data6 = json.load(json_file)
u6sm = (data6['documentSentiment']['magnitude']) 
u6ss = (data6['documentSentiment']['score'])

with open('tweets/u7_sentiment_output.json') as json_file:
    data7 = json.load(json_file)
u7sm = (data7['documentSentiment']['magnitude']) 
u7ss = (data7['documentSentiment']['score'])

with open('tweets/u8_sentiment_output.json') as json_file:
    data8 = json.load(json_file)
u8sm = (data8['documentSentiment']['magnitude']) 
u8ss = (data8['documentSentiment']['score'])

with open('tweets/u9_sentiment_output.json') as json_file:
    data9 = json.load(json_file)
u9sm = (data9['documentSentiment']['magnitude']) 
u9ss = (data9['documentSentiment']['score'])

with open('tweets/u10_sentiment_output.json') as json_file:
    data10 = json.load(json_file)
u10sm = (data10['documentSentiment']['magnitude']) 
u10ss = (data10['documentSentiment']['score'])


print("Now building the final report")

#now populate excel spreadsheet with tweet username and sentiment

from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

#put column headings in the sheet
sheet["A1"] = "Twitter User"
sheet["B1"] = "Tweet Magnitude"
sheet["C1"] = "Tweet Score"

#put user id in the sheet
sheet["A2"] = u1
sheet["A3"] = u2
sheet["A4"] = u3
sheet["A5"] = u4
sheet["A6"] = u5
sheet["A7"] = u6
sheet["A8"] = u7
sheet["A9"] = u8
sheet["A10"] = u9
sheet["A11"] = u10

#put users tweet magnitude in the sheet acceptable values 0 to infinity
sheet["B2"] = u1sm
sheet["B3"] = u2sm
sheet["B4"] = u3sm
sheet["B5"] = u4sm
sheet["B6"] = u5sm
sheet["B7"] = u6sm
sheet["B8"] = u7sm
sheet["B9"] = u8sm
sheet["B10"] = u9sm
sheet["B11"] = u10sm

#put users tweet score in the sheet
#The more negative the number the more negative the tweet
sheet["C2"] = u1ss
sheet["C3"] = u2ss
sheet["C4"] = u3ss
sheet["C5"] = u4ss
sheet["C6"] = u5ss
sheet["C7"] = u6ss
sheet["C8"] = u7ss
sheet["C9"] = u8ss
sheet["C10"] = u9ss
sheet["C11"] = u10ss

workbook.save(filename="Tweet_Sentiment_Report.xlsx")











