import requests


from gpiozero import Button
 
url = "https://maker.ifttt.com/trigger/button_pressed/with/key/eNlI6JlxNsgHsWbecsZZUErDcW_D3BbzHk_4B7Xd439"
 

req  = requests.get(url)
#print(req.status_code)

def onpressed():
    req1 = requests.get(url)
    print(req1.status_code)

button = Button(2) 

button.when_pressed = onpressed

#print(req.status_code)

#ifft = requests.get(url)
#print(ifft.status_code)