from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, esta é a sua mensagem exibida na página web!"

if __name__ == '__main__':
    app.run(debug=True)