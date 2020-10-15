# Project-2
Caleb Burke EC601 10/2/2020 Social Media Analyzer
This purpose of this project is to construct a media analyzer The media analyzer the is the python script tweetsearch will search 
today's Tweets that contain negative keywords related to flying and flights. It will then take 10 tweets and feed them into the 
Google NLP to determine the Sentiment. The analyzer then writes the User id from the twitter feed and Google NLP's Tweet magnitude 
and score into an Excel report that maps user ids to magnitude and score of the tweet itself.
This media analyzer could be used by:

1.	A federal air Marshall wants a list of today's twitter users that have a negative sentiment about flying so that he can examine 
user profiles for people on flights or in airports today that might be a problem for security on flights or in the airport
2.	The head of sales at Delta airlines wants to get screen names of anyone who is currently dissatisfied/or disenfranchised about 
flying so that she can target a new "Delta Cares" program designed to find new customers who currently use other carriers but are unhappy.

To Run.

go to the python_scripts folder and type python3 tweetsearch.py The output will be an excel spreadsheet in the same folder named 
Tweet_Sentiment_Report containing the user Id and tweet's sentiment magnitude and score.
score values 0 to +1 should be interpreted as positive score values 0 to -1 should be interpreted as negative magnitude values 
range from 0 to infinity and so a greater value represents a stronger feeling toward the score
Therefore the Air Marshall and sales people will be looking at users profiles with scores approaching -1 with a high magnitude.

Work left to be done*************************
1.	format the report for readability and highlight users to look at based on score
2.	have the scrip pick the most negative tweets and then open https://twitter.com/user_ID with the users profile to examine further
3.	restrict the information from twitter based on location

