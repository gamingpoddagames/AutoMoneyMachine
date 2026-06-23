from flask import render_template
import json


def load_articles():
    try:
        with open("data/articles.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def register_routes(app):

    @app.route("/")
    def home():

        articles = load_articles()

        return render_template(
            "index.html",
            articles=articles
        )
