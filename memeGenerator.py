import requests
import random
import paralleldots
import os

# ParallelDots for Emotion Analysis
api_key = os.environ['ParallelDots']
paralleldots.set_api_key( api_key )

emotions = {
    "Happy": [101470, 91538330, 5496396, 8072285, 101288, 16464531, 91545132, 101511, 100947, 84341851, 101440, 101716, 163573, 143601,10628640],
    "Angry": [405658, 97984, 563423, 405658, 91545132, 14230520, 245898, 222403160, 259680, 61580, 3218037, 195389, 718432, 124212, 1790995, 442575, 101711, 29617627, 61527],
    "Excited": [89370399, 119139145, 28251713, 235589, 61533, 61556, 101287, 61544, 101716, 460541],
    "Sad": [61539, 6235864, 405658, 14371066, 14230520, 196652226, 80707627, 766986, 100955, 13757816, 442575],
    "Fear": [102156234, 61520, 155067746, 27813981, 101511, 175540452, 148909805, 40945639, 61581, 61583, 442575, 101711],
    "Bored": [1509839, 4087833, 124055727, 61582, 16464531, 91545132, 100947, 61516, 84341851, 40945639, 9440985, 766986, 13757816, 1790995, 10628640]
}

# IMGFLIP Credentials
url = "https://api.imgflip.com/caption_image"
username = os.environ['imgflip_username']
passsword = os.environ['imgflip_password']

default_url = "https://i.imgflip.com/4e2rdx.jpg"

def getMeme(text):
    # Get Emotion
    apiResponse = paralleldots.emotion(text)
    apiResponse = apiResponse["emotion"]
    emotion = max(apiResponse, key=apiResponse.get)
    # print('Emotion:', emotion)
    
    # Generate a random template based on emotion
    template_id = random.choice(emotions[emotion])
    # print('>Template ID', template_id)

    # Check if the text has only word
    if ' ' in text:
        text0, text1 = text.split(' ', 1)
    else:
        text0 = text
        text1 = ''
    
    # print('>Meme', 'Text 0:', text0)
    # print('>Meme', 'Text 1:', text1)

    # Prepare for Meme Generation 🔥
    querystring = {
        'username': username,
        'password': passsword,
        'template_id': template_id,
        'text0': text0,
        'text1': text1
    }
    response = requests.request('POST', url, params=querystring).json()

    # Return MEME URL // In case the meme genration fails send a default response
    return response["data"]["url"] if response["success"] else default_url