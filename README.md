# Popular-YT-Video-Predictor


## Description
A self-inspired python project that utilizes Google's Youtube API in order to analyze popular trending videos in order to create/predict a new popular video.

## Implementation

### main.py
- Utilizes Google's Youtube APIs in order to receive data regarding Youtube's most recent trending videos in json format.
- Reads from the json file into a Pandas DataFrame for easier access and manipulation.
- Cleans the title words using Python's Natural Language Toolkit and other methodologies. 
- Stores the following information of a word: word, POS(part of speech), occurrences into a database using SQLite3

### title_generator.py
- Holds the definition for TitleGenerator class.
    - Generates titles from sentence formats
      - Four different types of title sentences to be generated: two simple structured formats and two intermediate structured formats.
    - Queries a word database in order to provide the appropriate components of a phrase based on its POS

## Final Thoughts
- In the future, I would possibly take this project one step further by improving the predictive sentence structures. Instead of using static linguistic sentence structures, I would consider manipulating neural networks to create sentences that are more accurate and make more sense. In addition, I would also consider implementing the ability to use these popular videos to predict other videos online that would become popular.
- In the end, this project was done as fun-short task to practice using APIs to retrieve data and store it in an SQL database. In addition, I had the opportunity to work with Python's Natural Language Tool-Kit to expose me to some of the concepts and capabilities of it. 

