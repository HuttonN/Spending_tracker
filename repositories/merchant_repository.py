from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, activated_merchant) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.activated]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id

def select_all():
    merchants = []

    sql = "SELECT * FROM merchants"
    results = run_sql(sql)

    for row in results:
        merchant = Merchant(row['name'], row['activated_merchant'], row['id'])
        merchants.append(merchant)
    return merchants

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def select(id):
    merchant = None 
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        merchant = Merchant(result["name"], result["activated_merchant"], result["id"])
    return merchant

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (name, activated_merchant) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.activated, merchant.id]
    run_sql(sql, values)