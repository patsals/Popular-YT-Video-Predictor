import json
from googleapiclient.discovery import build
import sqlite3
import pandas as pd
import nltk
import matplotlib.pyplot as plt
"""
Important notes:
- youtube api wasn't supporting some of the provided ISO 3166-1 alpha 2 codes of countries so
    they were disregarded in this project
- Nltk's library for languages is very small so only the countries where their languages were
    within the stopwords library were able to get considered
    https://stackoverflow.com/questions/54573853/nltk-available-languages-for-stopwords

"""
#youtube -> json -> to pandas df
# dataframe description words -> sql database (Word | POS | num occurrences)
#
#county codes: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
#most populated countries:https://www.worldometers.info/world-population/population-by-country/

API_KEY = "AIzaSyDqitOoj1fCMdzUHapDY358e5Ys4_yN4Os"
json_file_name = "mostPopularVideosByCountry.json"



def popular_videos_by_country_to_json(country, country_code):
    youtube = build('youtube', 'v3', developerKey= API_KEY)
    countryDict = {}
    with open(json_file_name, "w") as outfile:
        request = youtube.videos().list(part='snippet,contentDetails,statistics',
                                        chart= 'mostPopular', regionCode = country_code,
                                        maxResults= 100)
        response = request.execute()
        countryDict[country] = response
        json.dump(countryDict,outfile, indent= 4)



def json_to_df(country):
    with open(json_file_name) as infile:
        data = json.load(infile)
        df = pd.DataFrame({"id": ["0"], "title": [""], "views": [0], "likes": [0], "comments": [0], "description": [""]})
        for video in data[country]['items']:
            try:
                temp_df = pd.DataFrame(
                    {"id": video["id"], "title": [video["snippet"]["title"]], "views": [video["statistics"]["viewCount"]],
                     "likes": [video["statistics"]["likeCount"]], "comments": [video["statistics"]["commentCount"]],
                     "description": [video['snippet']['description']]})
            except KeyError as e:
                if str(e) == "\'likeCount\'":
                    temp_df = pd.DataFrame(
                        {"id": video["id"], "title": [video["snippet"]["title"]],
                         "views": [video["statistics"]["viewCount"]],
                         "likes": [video["statistics"]["favoriteCount"]], "comments": [video["statistics"]["commentCount"]],
                         "description": [video['snippet']['description']]})
                elif str(e) == "\'commentCount\'":
                    temp_df = pd.DataFrame(
                        {"id": video["id"], "title": [video["snippet"]["title"]],
                         "views": [video["statistics"]["viewCount"]],
                         "likes": [video["statistics"]["likeCount"]], "comments": [0],
                         "description": [video['snippet']['description']]})
            df = pd.concat([df, temp_df])
    return df



def get_word_dist(country, df_column):
    combined_description = " ".join([description for description in df_column])

    #filter out anything that isn't alphanumeric. eg: no links, emojis,...
    tokenizer = nltk.RegexpTokenizer('\w+')
    only_words = tokenizer.tokenize(combined_description)

    #stem the words to avoid repetition of occurances of similar instances of word
    new_words = filter_words(country, only_words)

    #get frequency
    frequency_dist = nltk.FreqDist(new_words)

    return frequency_dist



def filter_words(country, words):
    # utilize nltk's stopwords functionality to easily filter out additional words we dont want
    country_language = {"United States": "english", "Australia": "english",
                        "Brazil": "portuguese", "Mexico": "spanish", "Russia": "russian"}
    stop_words = set(nltk.corpus.stopwords.words(country_language[country]))

    # after examining, we want to remove additional words that are irrelevant
    irrelevant_words = ["http", "com", "www"]
    only_words = [word for word in words if word not in stop_words and word not in irrelevant_words]

    return only_words



def create_word_database(country, freqD):
    db_name = country.replace(" ", "") + "_popular_words"
    conn = sqlite3.connect(db_name + ".db")
    cur = conn.cursor()

    tagged_words = dict(nltk.pos_tag((freqD).keys()))
    word_stats = list(zip(tagged_words.keys(), tagged_words.values(), freqD.values()))
    word_stats = sorted(word_stats, key = lambda word: word[2], reverse = True)

    query = "DROP TABLE IF EXISTS " + db_name
    cur.execute(query)

    query = "CREATE TABLE " + db_name + "( " \
            "word TEXT UNIQUE PRIMARY KEY," \
            "POS TEXT," \
            "occurrences INTEGER)"
    cur.execute(query)

    for word in word_stats:
        query = "INSERT INTO " + db_name + "(word, POS, occurrences) " \
                "VALUES (?, ?, ?);"
        cur.execute(query, word)

    conn.commit()
    conn.close()



def get_freqd_visualization(country,frequencies):
    frequencies = sorted(dict(frequencies).items(), key = lambda x: x[1], reverse= True)[:25]
    x_values = [item[0] for item in frequencies]
    heights = [item[1] for item in frequencies]
    plt.bar(x_values,heights, align= "center")
    plt.title(country)
    plt.xticks(rotation = -45)
    plt.show()



def main():
    countries = {"United States": "US", "Brazil": "BR",
                 "Australia": "AU", "Russia": "RU", "Mexico": "MX"}
    country_dataframes = {}

    for country in countries.keys():
        popular_videos_by_country_to_json(country, countries[country])
        json_to_df(country)
        country_dataframes[country] = json_to_df(country)
        dist = get_word_dist(country, country_dataframes[country].title)
        create_word_database(country, dist)
        get_freqd_visualization(country,dist)


if __name__ == '__main__':
    main()


