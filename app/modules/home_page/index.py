from flask import Blueprint, render_template, request, Markup, redirect, url_for
from app import mongo

home_page = Blueprint('home_page', __name__)


@home_page.route('/')
def index():
    text_doc = mongo.db.editor.find_one({'_id': 1})
    if text_doc:
        value = Markup(text_doc['text'])
    else:
        value = ""
    return render_template('index.html', text=value)


@home_page.route('/tinymce')
def tinymce():
    return render_template('editors/tinymce.html')


@home_page.route('/mindup')
def mindup():
    return render_template('editors/mindup.html')


@home_page.route('/ckeditor', methods=['GET', 'POST'])
def ckeditor():
    if request.method == "GET":
        doc = mongo.db.editor.find_one({'_id': 1})
        if doc:
            text_doc = doc['text']
        else:
            text_doc = ""
        return render_template('editors/ckeditor.html', text=text_doc)

    elif request.method == "POST":
        data_edit = request.form['editor1']
        mongo.db.editor.update({"_id": 1}, {"text": data_edit}, True)
        return redirect(url_for('home_page.ckeditor'))
