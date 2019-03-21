#!/usr/bin/env python3
import json, requests
import pandas as pd
import csv
def main():
    r = requests.get("https://itunes.apple.com/search", params={
        'term': term,
        'country': cntry,
        'entity': type_str,
        'limit': 200
    })
    j = r.json()
        df = pd.DataFrame(j['results'])
        filename = term + "_" + type_str + ".csv"
        # df[['trackName', 'description']].to_csv(filename)
        df.to_csv(filename)
if __name__ == "__main__":
    main()