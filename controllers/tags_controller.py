from flask import Flask, render_template, request, redirect, Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

# INDEX
@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tag/index.html", tags = tags)

# NEW
@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tag/new.html")

# CREATE
@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    name = request.form["name"]
    activated = request.form["activated_tag"]
    new_tag = Tag(name, activated)
    tag_repository.save(new_tag)
    return redirect("/tags")

# DELETE
@tags_blueprint.route("/tags/<id>/delete", methods=["POST"])
def delete_tag(id):
    tag_repository.delete(id)
    return redirect("/tags")

# EDIT
@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tag/edit.html', tag=tag)

# UPDATE
@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    name = request.form["name"]
    activated = request.form["activated_tag"]
    tag = Tag(name, activated, id)
    tag_repository.update(tag)
    return redirect("/tags")