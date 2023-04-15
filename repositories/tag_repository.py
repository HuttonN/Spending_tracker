from db.run_sql import run_sql
from models.tag import Tag

def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['name'], row['id'])
        tags.append(tag)
    return tags

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)