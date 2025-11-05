# ===== MODULE IMPORTS =====
import webbrowser
import musicLibrary
import pywhatkit
from weather import getWeather
from news import News
from ai import aiProcess
from exchange import currency
from stocks import get_stock_price
from crypto import get_crypto_price
from autoEmail import retry
import stocksLibrary
import exLibrary
import time

# ===== HANDLE THE COMMAND RECEIVED ======
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://x.com")

    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)

    elif c.lower().startswith("weather"):
        city= c.lower().split("of")[1]
        getWeather(city)

    elif c.lower().startswith("take a note"):
        keyword= c.split("take a note")[1]
        with open ("Note.txt","w") as f:
            f.write(keyword)

    elif c.lower().startswith("convert"):
        value= c.lower().split()
        # Eg: value= "convert 1 dollar into rupees" or "convert $1 in rupees"
        try:
            b= value[2]
            base= exLibrary.cur[b]
            t= value[4]
            target= exLibrary.cur[t]
            amount= value[1]
            a= currency(base,target,amount)
            print(f"Amount in {t} is: {str(a)}")

        except IndexError as i:
            print("error")

        # If base & amount are consolidated
        except Exception as e:
            try:
                # Target:
                t= value[3]
                target= exLibrary.cur[t]
                # Split the {base + amount}:
                v= value[1]
                if (v[0]== "$"):
                    amount= v.lstrip("$")
                elif (v[0]== "€"):
                    amount= v.lstrip("€")
                b= v[0]
                base= exLibrary.cur[b]
                # Calculate:
                a= currency(base,target,amount)
                print(f"Amount in {t} is: {str(a)}")
            except IndexError as i:
                print("error")

    elif c.lower().startswith("crypto"):
        btc_price  = get_crypto_price("BTC", "INR")
        print(f"Current Bitcoin price: ₹{int(btc_price)}")
        eth_price  = get_crypto_price("ETH", "INR")
        print(f"Current Etherium price: ₹{int(eth_price)}")
        bnb_price  = get_crypto_price("BNB", "INR")
        print(f"Current Binance coin price: ₹{int(bnb_price)}")
        doge_price = get_crypto_price("DOGE", "INR")
        print(f"Current Doge coin price: ₹{int(doge_price)}")

    elif c.lower().startswith("write a mail"):
        retry()
        
    elif c.lower() == "what can you do":
        print("I can do the following tasks:    (with examples) \nopen websites: 'open google' \nplay music: 'play perfect' \nprovide weather report: 'weather of mumbai' \ntake notes: 'take a note, exams are posponded to....' \ndo currency conversion: 'convert $1 into inr' \ntrack crypto prices: 'crypto ....' \nsending emails: 'write a mail' \nsending whatsapp text: 'send a whatsapp to +91...' \nread top headlines: 'tell me some news' \nplay game: 'start game' \nget updated with latest stock prices: 'stock price of apple' \nask ai".title())

    elif "news" in c.lower():
        News()

    elif "game" in c.lower():
        try:
            from Rock_Paper_Scissor import game
            game()
        except Exception as e:
            return

    elif "stock" in c.lower():
        query= c.lower().split()
        for i in query:
            if i in stocksLibrary.name:
                s= stocksLibrary.name[i]
        g= get_stock_price(s)
        print(f"The latest price for {s} is ${int(g)}")

    elif "whatsapp" in c.lower():
        rec= c.split("+",1)[1]
        receiver= f"+{rec}"
        print("ok, What's your message ?")
        mess= input("Type your message: ")
        print(f"Sending the following message to: {receiver}")
        time.sleep(1)
        pywhatkit.sendwhatmsg_instantly(receiver,mess,12,tab_close= True)

    else:
        #Let ai handle the command
        output= aiProcess(c)
        filtered_Text = output.replace("*", "")              # filter "*"
        Filtered_text = filtered_Text.replace("#", "")       # filter "#"
        filtered_text = Filtered_text.replace("&quot;", "")  # filter "&quot;"
        print(filtered_text)

# ====== MAIN LOOP ======
if __name__== "__main__":
    print("Hi, I am Nell")
while True:
    command = input("What can I help with ? \n")
    if command:
        if command.lower() in ['exit', 'quit', 'stop']:
            print("Goodbye!")
            break
        processCommand(command)
