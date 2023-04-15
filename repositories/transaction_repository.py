from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag

def save(transaction):
    sql = "INSERT INTO transactions (amount, merchant_id, tag_id) VALUES (%s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.merchant.id, transaction.tag.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    transaction.id = id

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)