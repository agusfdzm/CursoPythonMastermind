import requests
from requests_html import HTMLSession, AsyncHTMLSession

URL = "https://www.pccomponentes.com/tarjeta-grafica-asus-prime-geforce-rtx-5070-oc-12gb-gddr7-reflex-2-rtx-ai-dlss4"

session = HTMLSession()

contenido = session.get(URL)

print(contenido)

buyZone = contenido.html.find("#btnsWishAddBuy")

print(buyZone)