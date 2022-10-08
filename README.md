# Forecasting Bitcoin Trend Using Sentiment Extraction From Twitter

Project developed during my Master's degree. The main goal is to predict Bitcoin's trend using sentiment extracted from Twitter's platform and correlate them with other custom market indicator. 
This project got positive results when correlating sentiment with custom market indicators.

## Abstract

Bitcoin is the first decentralized digital currency constituting a successful alternative economic system. As a result, the Bitcoin financial market occupies an important position in society, where it has gained increasing popularity. The correct prediction of this type of market can drastically reduce losses and maximize investor profits. One of the most popular aspects of predicting the cryptocurrency market is the analysis of sentiment in posts shared publicly on social networks. Currently, the Twitter platform generates millions of posts a day, which has attracted several researchers in search of problem solving using sentimental analysis in tweets.

With this evolution, it is intended to develop, through Artificial Intelligence (AI) techniques, models capable of predicting the Bitcoin trend based on daily sentimental analysis of posts made on the Twitter platform with Bitcoin’s historical data. Specifically, it is intended to assess whether sentiment positively influences the Bitcoin trend, and whether positive, neutral and negative feelings positively influence the Bitcoin trend in the same way. Finally, it is also objective to assess whether indicators such as market volume and the volume of tweets carried out within the scope of the Bitcoin theme positively influence its trend.

To validate the potential of the study, two AI models were developed. The first model was created to classify the sentiments of tweets into three typologies: positive, neutral and negative. This model focused on AI techniques based on Long Short Term Memory (LSTM), Bidirectional Long Short Term Memory (BI-LSTM) and Convolutional Neural Network (CNN). In turn, the second model was designed to classify Bitcoin’s future trends into strong uptrend, uptrend, downtrend and strong downtrend. In this sense, the model focused on AI techniques based on LSTM and Random Forest Classifier.

In general, it was possible to achieve good performance in the development of sentiment classification models, achieving an accuracy value of 87 % in the LSTM and BI-LSTM models and 86% in the model based on CNN technology. Regarding the model focused on predicting the Bitcoin trend, it was possible to validate that sentiment positively influences the Bitcoin trend prediction. More interestingly, neutral sentiment volume has a more significant impact on Bitcoin trend prediction. The Random Forest Classifier technique proved to be the best, recording accuracy of 57.35% in predicting the Bitcoin trend. Removing the sentiment variable made it possible to verify a cadence of 15% to 20% in the Bitcoin trend forecast, which effectively validates that sentiment positively influences the trend forecast.