from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/jrx2000', methods=['GET'])
def get_website():
    return render_template('jrx2000.html')


if __name__ == '__main__':
    app.run()
