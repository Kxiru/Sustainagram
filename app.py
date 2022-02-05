from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def method_name():
    return render_template('static/index.html')

if __name__ == "__main__":
    app.run()