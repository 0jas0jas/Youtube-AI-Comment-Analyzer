# -*- coding: utf-8 -*-

disallowedWords = ["the",
"of",
"to",
"and",
"a",
"in",
"is",
"it",
"you",
"that",
"he",
"was",
"for",
"on",
"are",
"with",
"as",
"I",
"his",
"they",
"be",
"at",
"one",
"have",
"this",
"from",
"or",
"had",
"by",
"not",
"word",
"but",
"what",
"some",
"we",
"can",
"out",
"other",
"were",
"all",
"there",
"when",
"up",
"use",
"your",
"how",
"said",
"an",
"each",
"she",
"which",
"do",
"their",
"time",
"if",
"will",
"way",
"about",
"many",
"then",
"them",
"write",
"would",
"like",
"so",
"these",
"her",
"long",
"make",
"thing",
"see",
"him",
"two",
"has",
"look",
"more",
"day",
"could",
"go",
"come",
"did",
"number",
"sound",
"no",
"most",
"people",
"my",
"over",
"know",
"water",
"than",
"call",
"first"]

import pyinputplus as pyip
from colorama import Fore, Style

from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.probability import FreqDist
import nltk

from spamDetection import model, vectorizer

from youtubeApi import youtube

from pprint import pprint
from urllib.parse import urlparse, parse_qs

vader = SentimentIntensityAnalyzer()

youtube = youtube()

commentArray = []

def topKeywords():
    words = []
    for comments in commentArray:
        words += comments.split()
    
    words = [x for x in words if x not in disallowedWords]

    keywords = nltk.Text(words)
    keywordDistribution = FreqDist(keywords)
    keywordDistribution.plot(80, cumulative=False)

    print("\n")
    print("\n")

    print(Fore.GREEN + "Top 10 keywords and their connotations (the more positive a word, the higher the percentage):")
    print(Style.RESET_ALL)

    total = 0
    for word, count in keywordDistribution.most_common(10):
        score = vader.polarity_scores(word)["compound"]
        score = score * 100
        total += score
        print(f"{word} occurs {count} times and has a positivity score of {score}%")
    print(f"The average positivity score of the top 10 keywords is {total/10}%")
    print("\n")
    print("\n")

def spamDetection():
    Model = model()
    tfidf_vectorizer = vectorizer()
    prediction = Model.predict(tfidf_vectorizer.transform(commentArray))

    spam = open("spam.txt", "w")
    ham = open("ham.txt", "w")

    spamCount = 0
    hamCount = 0

    for i in range(len(commentArray)):
        if prediction[i] == 1:
            try:
                spam.write(commentArray[i-1])
                spam.write("\n")
                spamCount += 1
            except: continue
        else:
            try: 
                ham.write(commentArray[i-1])
                ham.write("\n")
                hamCount += 1
            except: continue
    
    print(f"{spamCount} spam and {hamCount} legitimate comments were recognised in the comments out of the 100 comments.")
    print("spam comments were moved to" + Fore.RED + " spam.txt" + Style.RESET_ALL)
    print("legitimate comments were moved to" + Fore.GREEN + " ham.txt" + Style.RESET_ALL)
    spam.close()
    ham.close()

    
def getComments(id: str):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=id,
        textFormat="plainText",
        maxResults="100"
    )

    response = request.execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]
        author = comment["snippet"]["authorDisplayName"]
        commentText = comment["snippet"]["textDisplay"]

        commentArray.append(commentText)

print("Do you want to type in a URL or give an array of comments?")
result = pyip.inputMenu(["URL", "Array"])

if(result == "URL"):
    url = input("Please enter URL: ")
    url_data = urlparse(url)
    query = parse_qs(url_data.query)
    video = query["v"][0]

    getComments(video)

elif(result == "Array"):
    comments = input("Please enter comments separated by commas: ")
    
    commentArray = comments.split(",")

topKeywords()
spamDetection()

print(Style.RESET_ALL)