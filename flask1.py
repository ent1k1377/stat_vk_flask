from flask import Flask, render_template
from main import main, auth_handler

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    stat = main()
    actv = stat[0]
    ages = stat[1]
    city = stat[2]
    return render_template('base.html', actv=actv, ages=ages, city=city)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
