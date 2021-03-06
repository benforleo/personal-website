from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)


@app.route('/')
def portfolio():
    year = dt.datetime.now().year

    return render_template('portfolio.html', year=year)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run()

