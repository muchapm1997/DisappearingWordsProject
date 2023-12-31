from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_text():
    if request.method == 'POST':
        text = request.form['text']
        return render_template('index.html', saved_text=text)


if __name__ == '__main__':
    app.run(debug=True)
