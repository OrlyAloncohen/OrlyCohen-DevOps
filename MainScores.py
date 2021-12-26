from flask import Flask, render_template
from Utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def show_score():
    try:
        with open(SCORES_FILE_NAME, "w+") as f:
            user_score = int(f.readline())
    except:
        user_score = 0
    return render_template("orlyco.html", user_score=user_score)


if __name__ == '__main__':
    app.run()
