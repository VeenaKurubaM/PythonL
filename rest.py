import requests
def get(url):
    response=requests.get(url)
    if response.status_code==200:
        return response.text
    else:
        return None
   
text=get("https://veena-kuruba-portfolio-dev.lovable.app/")
print(text)


    
