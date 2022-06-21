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

https://youtu.be/WaJC30qKgYc