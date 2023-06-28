#!/usr/bin/python3
"""
Contains functions that handles request strings
"""
endpoint = 'https://www.googleapis.com/youtube/v3/search'
api_key = 'AIzaSyBIdZRCaifV3zjSALQXvYmBFPyf4BPpaYE'


def return_query(query):
    query = query.replace(' ', '+')
    query = query.replace('_', '+')
    return f'{endpoint}?key={api_key}&type=video&part=snippet&maxResults=10&q={query}'