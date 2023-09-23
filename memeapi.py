class memeApi():
    def __init__(self):
        pass

    def getgif(self, search, apikey, limit):
        import requests
        import json
        search_term = search
        r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, limit))
        if r.status_code == 200:
            top_8gifs = json.loads(r.content)
            return top_8gifs['results'][5]['media'][0]['mediumgif']['url']
        else:
            top_8gifs = None
    
    def getmeme(self):
        import requests
        import json
        r = requests.get("https://meme-api.com/gimme")
        if r.status_code == 200:
            meme = json.loads(r.content)
            return meme
        else:
            meme = None