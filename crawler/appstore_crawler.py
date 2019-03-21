#!/usr/bin/env python3
import json, requests
import pandas as pd
import csv
import sys

def userInput():
    type_list = ['movie', 'podcast', 'music', 'musicVideo', 'audiobook', 'shortFilm', 'tvShow', 'software', 'ebook', 'all']

    term = input("Please enter a word to search for: ")
    term = term.replace(" ", "+")

    print("Please enter the number of the type of results you want returnd ex) 1")
    print("1.movie 2.podcast 3.music 4.musicVideo 5.audiobook 6.shortFilm 7.tvShow 8.software(app) 9.ebook 10.all")
    type_num = input()
    type_str = type_list[int(type_num) - 1]
    print(type_str)

    cntry = input("Please enter the two-letter country code for the store you want to search: ")
    cntry = cntry.lower()
    if(len(cntry) == 0):
        cntry = 'us'
    elif(len(cntry) != 2):
        print("You've entered a wrong country code!")
        sys.exit(1)
    
    return [term, type_str, cntry]
        

def main():
    term, type_str, cntry = userInput()

    r = requests.get("https://itunes.apple.com/search", params={
        'term': term,
        'country': cntry,
        'entity': type_str,
        'limit': 200
    })
    j = r.json()
    
    if(j['resultCount'] > 0):
        df = pd.DataFrame(j['results'])
        filename = term + "_" + type_str + ".csv"
        # df[['trackName', 'description']].to_csv(filename)
        df.to_csv(filename)

        print("%d results" % j['resultCount'])
    else:
        print("No Results")


if __name__ == "__main__":
    main()