from flask import Flask,render_template

app = Flask(__name__)


    #definir rutas
@app.route('/')
def index():
        return render_template('index.html')

@app.route('/Registrar')
def saludos():
      return render_template('registrar.html')

if __name__ == '__main__':
    app.add_url_rule('/',view_func=index)
    app.run(debug=True,port=5005)