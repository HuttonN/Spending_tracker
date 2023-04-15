from flask import Flask, render_template, request, redirect, Blueprint
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

transactions_blueprint = Blueprint("spending_summary", __name__)

@transactions_blueprint.route("/spending_summary")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)