# Popular-YT-Video-Predictor (WIP)


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
    - Queries a word database in order to provide the appropriate components of a phrase based on its POS

## Final Thoughts

