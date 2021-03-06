from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import requests


GITHUB_TOKEN = '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'
GITHUB_USER = 'DSchmitz6320'

app = Flask(__name__)
app.config['SECRET_KEY'] = '47kJH438uihkjh438ohokjKJHle38'
ckeditor = CKEditor(app)
Bootstrap(app)

def get_projects():
    url = f"https://api.github.com/users/{GITHUB_USER}/repos"
    headers = {"Accept":"application/vnd.github.mercy-preview+json"}
    repos = requests.get(url, headers=headers, auth=(GITHUB_USER,GITHUB_TOKEN)).json()
    print(repos)
    print('FUUUUUUUUUUUUUUUU')
    projects = []
    for repo in repos:
        if repo["homepage"]:
            project = {
                "id": repo["id"],
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"],
                "topics":repo["topics"],
                "images": repo["homepage"].split(";")
            }
        projects.append(project)
    projects_split = [projects[x:x+3] for x in range(0, len(projects), 3)]

    return projects_split

@app.route('/')
def index():
    return render_template('index.html', all_projects=get_projects())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)