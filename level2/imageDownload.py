# download an image from an URL

import urllib.request
import sys

url = input("Enter the URL: ")
try:
  urllib.request.urlretrieve(url, "image.jpg")
  print("Imagem salva! =)")
except:
  erro = sys.exc_info()
  print("Ocorreu um erro:", erro)
