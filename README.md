# 🤖 Nell – Smart AI Assistant

Nell is a **Python-based smart personal AI assistant** designed to automate everyday digital tasks using **natural language text commands**. It reduces manual effort and enables smooth human–computer interaction through automation, real-time data processing, and AI-based decision handling.

---

## ✨ Features

Nell can perform a wide range of automated tasks:

* 🌐 Open websites (Google, YouTube, Facebook, Instagram, Twitter/X)
* 📧 Send emails
* 💬 Send WhatsApp messages
* 🎵 Play music from YouTube
* 🌦️ Get real-time weather reports
* 📰 Fetch top news headlines
* 📝 Take and manage notes
* 📈 Track stock prices
* ₿ Track cryptocurrency prices
* 💱 Currency conversion
* 🎮 Play games
* 🤖 Handle unknown queries using AI (conversational fallback)

---

## 🛠️ Technologies Used

* **Python**
* **Web Automation** (`webbrowser`, `pywhatkit`)
* **APIs** for weather, news, stocks, crypto, and currency exchange
* **Custom AI Module** for handling unknown queries
* **Modular Architecture** for scalability and maintainability

---

## 📂 Project Structure

```
Nell/
│
├── main.py                # Main assistant logic
├── ai.py                  # AI processing module
├── weather.py             # Weather fetching module
├── news.py                # News headlines module
├── crypto.py              # Cryptocurrency prices
├── stocks.py              # Stock prices
├── exchange.py            # Currency conversion
├── musicLibrary.py        # Music links
├── stocksLibrary.py       # Stock symbols
├── exLibrary.py           # Currency symbols
├── autoEmail.py           # Email automation
├── Rock_Paper_Scissor.py  # Game module
├── README.md              # Readme file
└── requirements.txt       # Required modules
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sourku0712/Nell.git
cd Nell
```

### 2️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

⚠️ Ensure you have an **active internet connection** for real-time data features.

### 3️⃣ Run the Assistant

```bash
python main.py
```

---

## 💬 Example Commands

```
open google
play perfect
write a mail
send a whatsapp to +91XXXXXXXXXX
weather of mumbai
take a note exams are postponed
convert $1 into inr
crypto
stock price of apple
tell me some news
```

To exit the assistant:

```
exit
```

---

## 🧠 AI Capability

If Nell encounters a command it doesn’t explicitly recognize, it forwards the query to its **AI module**, enabling conversational responses and flexible interaction.

---

## 🚀 Future Enhancements

* 🎙️ Voice command support
* 🖥️ GUI interface
* ⏰ Task scheduling
* 🌍 Multi-language support
* ☁️ Cloud deployment

---

## 🙌 Acknowledgments

This project demonstrates how **Python** can be used to build a smart, modular, and scalable AI assistant by integrating automation, APIs, and conversational intelligence.
