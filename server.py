from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')

def play():
    return render_template("index.html", num = 3, str = "blue")

@app.route('/play/<int:num>')

def multiple_boxes(num):
    return render_template("index.html", num = num)

@app.route('/play/<int:num>/<str>')

def color_boxes(num, str):
    return render_template("index.html", num = num, str = str)

if __name__=="__main__":
    app.run(debug=True)