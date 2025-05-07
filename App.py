import re
import textblob as tb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# This packages are installed at the beginning of the project
# nltk.download('punkt_tab')
# nltk.download('stopwords')


# Read the data from the csv file
df = pd.read_csv('./Instagram - Comments.csv')
ptComments = [] # positive comments list
ntComments = [] # negative comments list
nuComments = [] # neutral comments list

# get all comments from the csv file in array format
comments = np.array(df['comment'])

class SentimentAnalysis:
    def __init__(self, comments):
        self.comments = comments
        self.posComments = []
        self.negComments = []
        self.neuComments = []
    
    def get_comment_sentiment(self, comment):
        # Create a TextBlob object
        analysis = tb.TextBlob(str(comment))

        # Analysize the sentiment of the comment
        if analysis.sentiment.polarity > 0:
            # If the sentiment is positive, add it to the positive comments array
            self.posComments.append(comment)
            return 
        elif analysis.sentiment.polarity < 0:
            # If the sentiment is negative, add it to the negative comments array
            self.negComments.append(comment)
            return
        else:
            # If the sentiment is neutral, add it to the neutral comments array
            self.neuComments.append(comment)
            return
        
    def get_sentiment(self):
        # Loop through all comments and get their sentiment
        for comment in self.comments:
            self.get_comment_sentiment(comment)

        
    def get_sentimet_comments_list(self):
        # Get all comments from the array and analyze their sentiment
        return self.posComments, self.negComments, self.neuComments





def main():
    # Create an instance of the SentimentAnalysis class
    sa = SentimentAnalysis(comments)
    # Get the sentiment of each comment and store it in the respective lists
    sa.get_sentiment()
    # Get the positive, negative and neutral comments lists
    ptComments, ntComments, nuComments = sa.get_sentimet_comments_list()
    # Get Percentage of positive, negative and neutral comments
    ptPercent = round(100 *len(ptComments) / len(comments))
    ntPercent = round(100 *len(ntComments) / len(comments))
    nuPercent = round(100 *len(nuComments) / len(comments))
    x = ['Positive', 'Negative', 'Neutral']
    y = [ptPercent, ntPercent, nuPercent]
    # plot the Pie chart
    plt.pie(y,labels=x)
    plt.legend()
    plt.title('Sentiment Analysis of YouTube Comments')
    plt.show()

    print(" Positive Tweets percentage: ", ptPercent)
    print(" Negative Tweets percentage: ", ntPercent)
    print(" Neutral Tweets percentage: ", nuPercent)

if __name__ == "__main__":
    # Calling the main function
    main()
