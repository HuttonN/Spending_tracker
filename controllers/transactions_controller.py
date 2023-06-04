from flask import Flask, render_template, request, redirect, Blueprint
from models.transaction import Transaction
from models.tag import Tag
from models.merchant import Merchant
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import datetime
import pdb

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
    tag_id = request.form["tag_id"]
    merchant_id = request.form["merchant_id"]
    day = request.form.get("days")
    month = request.form.get("months")
    year = request.form.get("years")

    filtered_transactions = []
    total = 0

    for transaction in all_transactions:
            if not tag_id or tag_id == "" or transaction.tag.id == int(tag_id): 
                if not merchant_id or transaction.merchant.id == int(merchant_id):
                    if not day or day == "All days" or transaction.date.day == int(day):
                        if not month or month == "All months" or transaction.date.month == int(month):
                            if not year or year == "All years" or transaction.date.year == int(year):
                                filtered_transactions.append(transaction)
                                total += transaction.amount

    tags = tag_repository.select_all()
    tag = tag_repository.select(tag_id) if tag_id else None
    merchants = merchant_repository.select_all()
    merchant = merchant_repository.select(merchant_id) if merchant_id else None

    
    return render_template("transaction/filter.html", transactions = filtered_transactions, tags = tags, tag=tag, merchant=merchant, merchants = merchants, total = total)
