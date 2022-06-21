# YouTube AI Comment Analyser

## What does it do?
It uses a few tools to analyse and display data about a youtube video's comment section including keyword frequency, sentiment analyser and spam and fraud comments detection.

## How to make it work.
- Clone this repository 
```
git clone https://github.com/0jas0jas/Youtube-AI-Comment-Analyzer
```

- In a terminal with PyPI installed execute the following to install dependencies
```
pip install -r requirements.txt
```

- Once all dependencies are installed, the program can run using this command run in the directory where this repository was cloned
```
python3 youtubeAI.py
```

- The program will give a detailed pathway to continue

## Usage Documentation
The entire program is run by three python files, "youtubeAI.py" being the main file. 'youtubeApi.py' stores information nessasary to send requests to Google's YouTube API. 'spamDetection.py' contains an AI model to predict if a comment can be classified as spam or fraud or not.

## The procedures

- topKeywords()
        This procedure looks at the commentArray which is a list of 100 comments from the YouTube link or a list of the comments that has been provided to the program. It outputs a visualisation of the top 80 keywords (excluding the most common 84 words of the english language) and outputs the top 10 most used words with their sentiment analysis.
    
- spamDection()
        This procedure imports an AI model from `spamDetection.py` and predicts whether the comments in the commentArray list are spam/fraud or not. It displays these predictions using quantitative statistics and saves all the spam comments in a separate file "spam.txt" which will appear with "ham.txt" (containing all the legitimate comments).

- getComments()
        When provided with a videoID, this procedure will append to the global list `CommentArray` using the Google YouTube API. This procedure prepares the data on which the upper two procedures work.

## Demo of the program

![Demo Video](https://youtu.be/WaJC30qKgYc)