# Sentiment-Analysis-of-the-NBA
Data Science Capstone Project exploring the question: Is all publicity good publicity? Through Sentiment Analysis of the NBA and its effect on game-to-game attendance.

## Summary
In the realm of combat sports, both negative publicity and positive publicity drive attendance to matches. I wondered, does this also apply to team sports? To explore this, I decided to do a Sentiment Analysis of tweets of five NBA teams during the 2018-2019 regular season and seeing if there is an effect on game-to-game attendance.

## Data
#### Tweets
Each team's tweet dataset was taken from Twitter using the GetOldTweets3 library. Search queries for the tweets gathered consisted of the team, and the top three players of each team. Tweets were only taken from cities with an NBA team and tweets were taken only during the 2018-2019 regular season (October 2018 - April 2019).
#### Training Data
Training data was pre-labelled tweets taken from the SemEval Project and the Sentiment140 Project. Pre-trained word embeddings for the neural network model was taken from the GloVe project.
#### Attendance Data
Attendance data was taken from https://www.basketball-reference.com/.
#### Arena Capacity Data
Arena Capacity Data was taken from https://en.wikipedia.org/wiki/List_of_National_Basketball_Association_arenas.

## Models
Two models were fitted for the Sentiment Analysis: 
1. Bag of Words Model with TFIDF Vectorization
2. Recurrent Neural Network using pre-trained GloVe Embeddings

## Analysis
With an accuracy of ~71% for both models, the simpler Bag of Words Model was used for the sentiment analysis. Once tweets have had their sentiments labelled, the polarized sentiment ratio was calculated by taking all the positive and negative tweets prior to a game and dividing that by all tweets prior to a game. 

Attendance ratio for games was calculated by taking the attendance numbers divided by the capacity of the arena.

To determine if there is an effect that the sentiment effects game-to-game attendance, the polarized sentiment ratio and attendance ratio are put into a linear regression to see if there is a relationship or not. 

## Results
Unfortunately, there is not enough evidence to conclude that tweet sentiment prior to games has an effect on attendance for any of these teams. Games for most of these teams sell out, regardless of tweet sentiment.

## Future Analysis
Future extensions on this project will focus on season-to-season attendance rather than game-to-game attendance. Incorporating smaller market teams and other social media platforms such as Reddit or Instagram are also planned.
