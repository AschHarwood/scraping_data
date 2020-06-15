import csv


import requests


import json


from bs4 import BeautifulSoup


apikey = config.apikey


api_url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&key=' + config.apikey






api_response = requests.get(api_url)


videos = json.loads(api_response.text)








with open("youtube_vides_5.csv", "w", encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["publishedAt", "title", "description", "thumbnailurl"])
    has_another_page = True
    while has_another_page:
        if videos.get("items") is not None:
            for video in videos.get("items"):
                video_data_row = [
                    video['snippet']['publishedAt'],
                    video['snippet']['title'],
                    video['snippet']['description'],
                    video['snippet']['thumbnails']['default']['url']]
                csv_writer.writerow(video_data_row)
        if "nextPageToken" in videos.keys():
            next_page_url = api_url + "&pageToken=" + videos["nextPageToken"]
            next_page_posts = requests.get(next_page_url)
            videos = json.loads(next_page_posts.text)
        else:
            print("no more videosget_ipython().getoutput("") ")
            has_another_page = False
            


#page 149

import csv
import json

import requests
channel_id = "UCJFp8uSYCjXOMnkUyb3CQ3Q"
youtube_api_key = config.apikey


import config






