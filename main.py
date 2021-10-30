from flask import Flask, render_template, request,url_for
from flask_bootstrap import Bootstrap
import time


app = Flask(__name__)
Bootstrap(app)



@app.route("/")
def home():
    return render_template("index.html")


@app.route('/write', methods = ['GET', 'POST'])
def write():

    # Onpresskey in the form tag in write.html submits the form each time any key is pressed.
    # Everytime the form is being submitted due to a key press, this post method is getting triggered agaib
    # and again.
    # Once the user stops typing, the last triggered post method executes the time.sleep code snippet
    # and everything written disappears. after 3 second.
    if request.method == 'POST':
        time.sleep(3)
        # return redirect('/write')
    return render_template("write.html")


if __name__ == '__main__':
    app.run(debug=True)

# MORE THINGS TO IMPLEMENT
# 1) Word count by accesing the input(my_id = request.form.get('writetext','')
# 2) Session timer.