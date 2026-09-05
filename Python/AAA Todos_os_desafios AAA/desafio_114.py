import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')

except urllib.error.URLError:
    print('sem pudim pra tu hoje 😂')

else:
    print('toma pudim 🍮')
