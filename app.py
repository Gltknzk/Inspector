from flask import Flask, jsonify, render_template
from flask_swagger import swagger
import re

app = Flask(__name__)

@app.route("/")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "v.1.0"
    swag['info']['title'] = "Welcome to Datatera Beta"
    return jsonify(swag)

@app.route('/api')
def get_api():
    return render_template('swaggerui.html')

#Check Credit Card Number
@app.route("/beta/checkcreditcardno/<string:candidate_value>", methods=["GET"], endpoint='check_credit_card_no')
def check_credit_card_no(candidate_value):

  candidate_value = re.sub('\D', '', str(candidate_value))
  x = re.search("^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$", candidate_value)

  if x:
   return jsonify(f"Credit Card Number is detected!!")
  else:
   return jsonify(f"No Credit Card Number is detected!!")
