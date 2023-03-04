from flask import Flask, session, flash, request, render_template, redirect, g
from babel.numbers import get_currency_symbol
from api_handles import get_symbols, convert_currency
from handle_messages import handle_messages


app = Flask(__name__)

app.config['SECRET_KEY'] = "IAMCOOL1234"


@app.route("/", methods=["GET", "POST"])
def convert():
    """
    Render the base HTML template if the HTTP method is GET, or process
    a conversion request if the HTTP method is POST. If a conversion request
    is made, store the conversion parameters in the session object and redirect
    to the "/rate-response" route.
    """

    if request.method == "POST":
        convert_from = request.form["convert_from"]
        convert_to = request.form["convert_to"]
        amount = request.form["amount"]

        session["convert_from"] = convert_from
        session["convert_to"] = convert_to
        session["amount"] = amount

        return redirect("/rate-response")
    return render_template("base.html")


@app.route("/rate-response")
def rate_response():
    """
    Retrieve the stored conversion parameters from the session object and use
    them to compute the conversion rate. If there are any error messages, redirect
    the user to the base route ("/") and display the messages. Otherwise, remove
    the stored conversion parameters from the session object and render the base
    HTML template with the conversion rate.
    """

    convert_from = session.get("convert_from")
    convert_to = session.get("convert_to")
    amount = session.get("amount")

    currency_symbol = get_currency_symbol(convert_to, 'en_US')
    rate_result = convert_currency(convert_from, convert_to, amount)
    symbol_lst = get_symbols()

    messages = handle_messages(convert_from, convert_to, amount, symbol_lst)

    if messages:
        for message in messages:
            flash(message)
        session.pop("convert_from", None)
        session.pop("convert_to", None)
        session.pop("amount", None)
        return redirect('/')

    session.pop("convert_from", None)
    session.pop("convert_to", None)
    session.pop("amount", None)

    return render_template("base.html", amount=amount, convert_from=convert_from, convert_to=convert_to, currency_symbol=currency_symbol, rate_result=rate_result)
