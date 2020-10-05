# external libraries
import re
from math import ceil

def shorten_url(url):
    # get rid of http(s) and www so encryption isn't influenced
    rec = re.compile(r"https?://(www\.)?")
    url = rec.sub('', url)

    # convert the url to hexadecimal
    encoded_url = url.encode("hex")

    # break up the url into segments of 5 characters, and add together 
    # this ensures that the maximum length of the url will not exceed 
    # 6 characters (for all practical purposes)
    n = len(encoded_url)
    while n > 6:
        segments = [int(encoded_url[i:i+5],16) for i in range(int(ceil(n/6)))]
        encoded_url = str(sum(segments))
        n = len(encoded_url)
    return "aakif.url/" + encoded_url