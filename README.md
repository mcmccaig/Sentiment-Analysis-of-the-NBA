<p align="center">
  <a href="" rel="noopener">
 <img width=400px height=200px src="Graphs/nbalogo.jpg" alt="Project logo"></a>
</p>

---

# Sentiment Analysis of the NBA
A Data Science Capstone Project exploring the question: "Is all publicity good publicity?" through natural language processing on NBA tweets.


## Summary
In the realm of combat sports, both negative publicity and positive publicity drive attendance to events. I wondered, does this also apply to team sports? To explore this, I decided to do a Sentiment Analysis of five NBA team's tweets and mentions during the 2018-2019 regular season and seeing if there is an effect on game-to-game attendance.

## Setup
After forking the repository, there one further step needed due to file size limitations.

#### Data
The RNN model takes advantage of pre-trained embeddings produced by GloVe. The file path and link for download are provided below. Please ensure to unzip the compressed files and have the .txt files within the file directory.

GloVe | Pre-Trained Twitter Word Vectors [[Link](http://nlp.stanford.edu/data/glove.twitter.27B.zip)]
```
- data/glove.twitter.27B/glove.twitter.27B.25d.txt
- data/glove.twitter.27B/glove.twitter.27B.50d.txt
- data/glove.twitter.27B/glove.twitter.27B.75d.txt
- data/glove.twitter.27B/glove.twitter.27B.100d.txt
```

Remaining datasets are within the repository in their proper directories.

#### Libraries
```
Python
- pandas
- numpy
- matplotlib
- GetOldTweets3
- requests
- sklearn
- xgboost
- keras (ver 2.2.4)
- tensorflow (ver 1.9.0)
- nltk
- gensim
```

## Scripts
Scripts are provided to scrape the datasets from the web. Can be found here [[Link](https://github.com/mcmccaig/Sentiment-Analysis-of-the-NBA/tree/master/Scripts)]

## Datasets
#### Tweets
Each team's tweet dataset was taken from Twitter using the GetOldTweets3 library. Search queries for the tweets gathered consisted of the team, and the top three players of each team. Tweets were only taken from cities with an NBA team and tweets were taken only during the 2018-2019 regular season (October 2018 - April 2019).
#### Training Data
Training data was pre-labelled tweets taken from the SemEval Project [[Link](http://alt.qcri.org/semeval2016/task4/)] and the Sentiment140 Project [[Link](http://help.sentiment140.com/for-students)]. Pre-trained word embeddings for the neural network model was taken from the GloVe project [[Link](https://nlp.stanford.edu/projects/glove/)].
#### Attendance Data
Attendance data was taken from Basketball-Reference [[Link](https://www.basketball-reference.com/)].
#### Arena Capacity Data
Arena Capacity Data was taken from Wikipedia [[Link](https://en.wikipedia.org/wiki/List_of_National_Basketball_Association_arenas)].

## Models
Two models were fitted for the Sentiment Analysis:
1. Bag of Words Model with TFIDF Vectorization
2. Recurrent Neural Network using pre-trained GloVe Embeddings

## Analysis
Final Report can be found here: [[Link](https://github.com/mcmccaig/Sentiment-Analysis-of-the-NBA/blob/master/Final%20Report.pdf)]

## Acknowledgements
Thank you to instructors and mentors Aaron Quinton and Boris Shabash of BrainStation, who provided hours of guidance and assistance in this analysis.
