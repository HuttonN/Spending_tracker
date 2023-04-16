from flask import Flask, render_template, request, redirect, Blueprint
from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant
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

# NEW
@transactions_blueprint.route("/spending_summary/new")
def new_transaction():
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template("transaction/new.html", merchants=merchants, tags=tags)

# CREATE
@transactions_blueprint.route("/spending_summary", methods=["POST"])
def create_transaction():
    amount = request.form["amount"]
    merchant_id = request.form["merchant_id"]
    tag_id = request.form["tag_id"]
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(amount,merchant,tag)
    transaction_repository.save(new_transaction)
    return redirect("/spending_summary")