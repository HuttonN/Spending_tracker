from flask import Flask, render_template, request, redirect, Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

# INDEX
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchant/index.html", merchants = merchants)

# NEW
@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchant/new.html")

# CREATE
@merchants_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form["name"]
    activated = request.form['activated_merchant']
    new_merchant = Merchant(name, activated)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")

# DELETE
@merchants_blueprint.route("/merchants/<id>/delete", methods=["POST"])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")

# EDIT
@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchant/edit.html', merchant=merchant)

# UPDATE
@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    activated = request.form['activated_merchant']
    merchant = Merchant(name, activated, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")

