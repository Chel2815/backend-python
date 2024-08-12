from flask import Flask
app = Flask(__name__) # Explicação abaixo da variável __name__
@app.route('/')
def hello_world():
 return 'Hello, World!'
if __name__ == '__main__':
 app.run(debug=True)
