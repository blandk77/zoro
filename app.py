from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Status: Working.....🎉'


if __name__ == "__main__":
    app.run()

#Added By @Telegram_Guyz
#Telegram Channel - @The_TGguy
#TG ID - @Itsme123c
