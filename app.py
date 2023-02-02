from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    str = 'whm Hello'
    return render_template('index.html', str=str)

if __name__ == '__main__':
    app.run(debug=True)
