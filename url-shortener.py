from pyshorteners import Shortener

url = 'http://www.google.com'

url_shortener = Shortener(user_id = "your id", api_key = "your key", type = int)
print("Short url is {}".format(url_shortener.adfly.short(url)))
