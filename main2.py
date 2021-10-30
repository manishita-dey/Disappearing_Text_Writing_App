from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
import time
import keyboard
from werkzeug.utils import redirect

DISAPPEAR_TIME = 5
my_id = None

app = Flask(__name__)
Bootstrap(app)


def countdown(t):
    while t > 0:
        if t > 0:
            time.sleep(1)
            t -= 1
        else:
            pass


def executeSomething():
    # code here
    time.sleep(5)
    global my_id
    my_id


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/write', methods=['GET', 'POST'])
def write():
    # form = RegistrationForm()

    if form.validate_on_submit():
        # do stuff with valid form
        # then redirect to "end" the form
        my_id = request.form.get('writetext','')
        print(my_id)
        return redirect(url_for('register'))


    return render_template("write.html")


def disappear_text():
    pass


if __name__ == '__main__':
    app.run(debug=True)