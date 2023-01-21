
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from datetime import date
from datetime import datetime
from dateutil import relativedelta

app = Flask(__name__, template_folder='/home/vijayruler/mysite/templates/')

@app.route('/')
def hello_world():
    cams_exp = getCompanyExp('4/4/2016', '1/7/2016')
    vamsoft_exp = getCompanyExp('23/8/2017', '3/4/2019')
    virtusa_exp = getCompanyExp('5/7/2019', '30/4/2021')
    accenture_exp = getCompanyExp('7/5/2021', date.today())
    cumulative = cams_exp + vamsoft_exp + virtusa_exp + accenture_exp
    cumulative_days = cumulative.days
    cumulative.months += (cumulative_days//30)
    cumulative.days = cumulative_days%30
    normalized_total = cumulative.normalized()

    return render_template("index.html", cams_exp = cams_exp, vamsoft_exp = vamsoft_exp, virtusa_exp = virtusa_exp,
            accenture_exp = accenture_exp, normalized_total = normalized_total)

def getCompanyExp(date1, date2):
    is_string = type(date2) == str

    start_date = datetime.strptime(date1, "%d/%m/%Y")
    if is_string:
        end_date = datetime.strptime(date2, "%d/%m/%Y")
    else:
        end_date = date2

    delta = relativedelta.relativedelta(end_date, start_date)
    delta.days += 1
    return delta