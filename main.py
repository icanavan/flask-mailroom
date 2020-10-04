import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation
from model import Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        donor = Donor.select().where(Donor.name == request.form['name']).get()
        # donor.save()  # No need to save the donor: if you're able to retrieve them from the database that means they're already saved.
        donation = Donation(value=request.form['donation-amount'], donor=donor)  # After retrieving the donor in the previous line, you can provide them to the `Donation` constructor like so.
        donation.save()
        return redirect(url_for('donations'))
    else:
        return render_template('create.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

