from flask import Flask, render_template, request, redirect, Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchant/index.html", merchants = merchants)