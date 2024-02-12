from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "<h3><b>Миссия Колонизация Марса</b></h3>"


@app.route('/index')
def index():
    return "<h3><b>И на Марсе будут яблони цвести!</b></h3>"


@app.route('/promotion')
def promotion():
    return "<h3>Человечество вырастает из детства.<br>" \
           "Человечеству мала одна планета.<br>" \
           "Мы сделаем обитаемыми безжизненные пока планеты.<br>" \
           "И начнем с Марса!<br>" \
           "Присоединяйся!<br>"


@app.route('/image_mars')
def image_mars():
    return "<h1>Жди нас, Марс!</h1>\n" \
           f'<img src="/static/img/mars.avif">'


@app.route('/promotion_image')
def promotion_image():
    with open('promotion_image.html', encoding='UTF-8') as html:
        return html.read()


@app.route('/astronaut_selection')
def astronaut_selection():
    with open('astronaut_selection.html', encoding='UTF-8') as html:
        return html.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
