from flask import Flask, render_template, request, redirect, Blueprint
from models.transaction import Transaction
from models.tag import Tag
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transactions_blueprint = Blueprint("spending_summary", __name__)

@transactions_blueprint.route("/spending_summary")
def transactions():
    transactions = transaction_repository.select_all()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    total = transaction_repository.total_sum()
    return render_template("transaction/index.html", transactions = transactions, tags = tags, merchants = merchants, total = total)