import requests
import shutil 
import os

###### Verion One #######
url:str = input("Enter URL here:::")
file_name:str = input("Enter file name here:::")
base, ext = os.path.splitext(file_name)

res = requests.get(url,stream =True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
        
    print('Image sucessfully Downloaded: ',file_name)
    os.rename(file_name, base + ".png")
else:
    print('Image Couldn\'t be retrieved')



