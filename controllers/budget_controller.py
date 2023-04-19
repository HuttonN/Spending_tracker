from flask import Flask, render_template, request, redirect, Blueprint

budget_blueprint = Blueprint("budget", __name__)

# INDEX
@budget_blueprint.route("/budgeting")
def budget():
    return render_template("budget/index.html")