from flask import Flask,request,redirect,url_for,render_template,jsonify
import json
app = Flask(__name__)


@app.route('/')
def welcome():
    return "welcome to home page"   

@app.route('/cal', methods=["GET"])
def math_operators():
    operation= request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operation == "addition":
        result=int(number1)+int(number2)
    elif operation=="subtraction":
        result=int(number1)-int(number2)
    elif operation=="multiplication":
        result=int(number1)*int(number2)
    else:
        result=int(number1)/int(number2)

    return jsonify(result)

if __name__ =="__main__":
    app.run(debug=True)
