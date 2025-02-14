from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Merhaba, bu uygulama Render üzerinde çalışıyor!"

if __name__ == '__main__':
    app.run()
