import requests

url = "https://odds.p.rapidapi.com/v1/odds"

querystring = {"region":"us","sport":"baseball_mlb","oddsFormat":"american","market":"h2h","dateFormat":"iso"}

headers = {
	"X-RapidAPI-Host": "odds.p.rapidapi.com",
	"X-RapidAPI-Key": "b501e0bf75mshf881260fcf61406p1a7f13jsnbce859978dd1"
}

response = requests.request("GET", url, headers=headers, params=querystring)

res = (response.text)
