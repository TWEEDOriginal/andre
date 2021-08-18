from flask import Blueprint, render_template,request,url_for,redirect


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('views.thankyou'))
    return render_template("index.html")


@views.route('/thankyou', methods=['GET', 'POST'])
def thankyou():
    return render_template("thankyou.html")