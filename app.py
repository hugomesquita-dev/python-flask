import db
from flask import Flask, abort, url_for

app = Flask(__name__)


@app.route("/")
def index():
    html = ["<ul>"]
    for username, user in db.users.items():
        html.append(
            #f"<li><a href='/user/{username}'>{user['name']}</a></li>"
            f"<li><a href='{url_for('user', username=username)}'>{user['name']}</a></li>"
        )
    html.append("</ul>")
    return "\n".join(html)

def profile(username):
    user = db.users.get(username)

    if user:
        return f"""
            <h1>{user['name']}</h1><br/>
            telefone{user['tel']}<br/>
            <a href="/">Voltar</a>
        """
    else:
        return abort(404, "Usuario não encontrado!!")


app.add_url_rule("/user/<username>/", view_func=profile, endpoint="user")

app.run(use_reloader=True)