
import websocket
import json
import time

def on_message(ws, message):
    print(message)
    veri = message.split()
    data = veri[-1]
    data = data.replace("'","")
    data = data.replace("}","")
    data = data.replace('"',"")
    son_mesaj = atbash(data)
    x = json.dumps({"type":"REGISTER","name":"abdullah","surname":"adanir","email":"abdullahadnir2147@gmail.com","registrationKey": son_mesaj})
    ws.send(x)
    print("gönderildi")
    time.sleep(10)

def atbash(text):

    result = ""
    for char in text:
        #Küçük harfler
        if char.islower():
            result += chr(219 - ord(char))
        else:
            result += char
    return result


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://cekirdektenyetisenler.kartaca.com/ws",
                                on_message = on_message
                                )
    ws.run_forever()
    


