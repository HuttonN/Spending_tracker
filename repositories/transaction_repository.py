from db.run_sql import run_sql
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
from models.tag import Tag
import repositories.tag_repository as tag_repository
from models.transaction import Transaction
from datetime import datetime

def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id, transaction_date) VALUES (%s, %s, %s, %s) RETURNING id"
    formatted_date = transaction.date.strftime('%Y-%m-%d')
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id, formatted_date]
    results = run_sql(sql,values)
    id = results[0]['id']
    transaction.id = id

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], merchant, tag, result["transaction_date"], result["id"])
        transactions.append(transaction)
    return transactions

def total_sum():
    total = 0
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        total += result["amount"]
    return total

def select_all_sort_ascend():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], merchant, tag, result["transaction_date"], result["id"])
        transactions.append(transaction)
    transactions.sort(key=lambda r: r.date)
    return transactions

def select_all_sort_descend():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], merchant, tag, result["transaction_date"], result["id"])
        transactions.append(transaction)
    transactions.sort(key=lambda r: r.date, reverse = True)
    return transactions

def select_all_filter_tag(tag):
    transactions = []
    sql = "SELECT * FROM transactions WHERE tag_id=%s"
    values = [tag.id]
    results = run_sql(sql, values)
    for result in results:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(result["amount"], merchant, tag, result["transaction_date"], result["id"])
        transactions.append(transaction)
    return transactions