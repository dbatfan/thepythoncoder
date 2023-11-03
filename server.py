from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('./webserver/static/database.txt', mode='a') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        database.write(f'\n{name},{email},{message}')


def write_to_csv(data):
    with open('./webserver/static/database.csv', mode='a', newline='') as database1:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            write_to_file(data)
            return redirect('/success.html')
        except:
            return 'Sorry! we have not got your Message,Kindly Retry'
    else:
        return 'Something went wrong. Try again!'

# @app.route("/generic.html")
# def generics():
#     return render_template('generic.html')
#
# @app.route("/elements.html")
# def elements():
#     return render_template('elements.html')
# dynamically handling page callout

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     return 'Form Submitted hoooorraaayyy!'
