import http.client

text = input("Enter the text: ")
language = input("Enter Language (pt, en, etc): ")

conn = http.client.HTTPSConnection("text-translator2.p.rapidapi.com")

payload = f"source_language={language}&target_language=id&text={text}"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'X-RapidAPI-Key': "9b2173be03msh2c3c609ea6a9908p135302jsndc427fe44fce",
    'X-RapidAPI-Host': "text-translator2.p.rapidapi.com"
}

conn.request("POST", "/translate", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))