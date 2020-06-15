import csv
import json

import requests
channel_id = "UCJFp8uSYCjXOMnkUyb3CQ3Q"
youtube_api_key = config.apikey

base = "https://www.googleapis.com/youtube/v3/search?"

fields = "&part=snippet&channelId="
api_key = "&key=" + youtube_api_key
api_url = base + fields + channel_id + api_key
