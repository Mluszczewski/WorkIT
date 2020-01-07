from flask import render_template, request
from workit.forms import SearchForm
from workit import app, collection
from workit.const import CATEGORIES, WEBSITES


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            offers = collection.find({})
        else:
            offers = collection.find({})
        return render_template(
                "home.html",
                offers=offers,
                categories=CATEGORIES,
                form=form
            )
    else:
        if collection.count_documents({}) == 0:
            for website in WEBSITES:
                website.create_offers()
                collection.insert_many(
                    [dict(offer) for offer in website.offers]
                )
        return render_template(
            "home.html",
            offers=collection.find({}),
            categories=CATEGORIES,
            form=form
        )