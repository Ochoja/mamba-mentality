#!/usr/bin/python3
"""
Contains functions that handles request strings
"""
endpoint = 'https://www.googleapis.com/youtube/v3/search'
api_key = 'AIzaSyA8hJNd4cbYyaLtxQG8dSdAuxvgm8OQNSM'


def return_query(query):
    return f'{endpoint}?key={api_key}&type=video&part=snippet&maxResults=10&q={query}'