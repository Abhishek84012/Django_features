from urllib.request import urlopen

with urlopen("url") as r:
    source = r.read()
