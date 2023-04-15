from db.run_sql import run_sql
from models.merchant import Merchant
from models.tag import Tag

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)