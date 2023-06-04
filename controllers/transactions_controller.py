from flask import Flask, render_template, request, redirect, Blueprint
from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import datetime

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
    date = request.form["transaction_date"]
    split_date = date.split('-')
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    new_transaction = Transaction(amount,merchant,tag, date)
    transaction_repository.save(new_transaction)
    return redirect("/spending_summary")

# SORT(ascend)
@transactions_blueprint.route("/spending_summary/sort_ascend")
def sort_transactions_ascend():
    transactions = transaction_repository.select_all_sort_ascend()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    total = transaction_repository.total_sum()
    return render_template("transaction/index.html", transactions = transactions, tags = tags, merchants = merchants, total = total)

# SORT(descend)
@transactions_blueprint.route("/spending_summary/sort_descend")
def sort_transactions_descend():
    transactions = transaction_repository.select_all_sort_descend()
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    total = transaction_repository.total_sum()
    return render_template("transaction/index.html", transactions = transactions, tags = tags, merchants = merchants, total = total)

# Filter tags
@transactions_blueprint.route("/spending_summary/filter", methods =['POST'])
def filter_transactions_tags_merchants():
    all_transactions = transaction_repository.select_all()
    tag_id = request.form.get("tag_id")
    if tag_id =="":
        tag_id = None
    merchant_id = request.form.get("merchant_id")
    if merchant_id =="":
        merchant_id = None
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    total = 0
    filtered_transactions = []
    
    for transaction in all_transactions:
        if tag_id is None or (tag_id == "" or transaction.tag.id == int(tag_id)):
            if merchant_id is None or (merchant_id == "" or transaction.merchant.id == int(merchant_id)):
                filtered_transactions.append(transaction)
                total += transaction.amount


    return render_template("transaction/filter.html", transactions = filtered_transactions, tags = tags, merchants = merchants, total = total)