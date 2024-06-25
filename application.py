from flask import Flask,render_template

FAI=Flask(__name__)


@FAI.route('/staticfiles')

def staticfiles():
    return render_template('staticfiles.html')


@FAI.route('/rr')
def rr():
    return render_template('rr.html')

FAI.run(debug=True)
