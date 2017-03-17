from flask import Flask, render_template, jsonify, request, url_for
from bridge import *
app = Flask(__name__)

@app.route('/')
def main():
    return render_template( 'index.html' )

@app.route('/send/', methods=['POST'])
def send():
    message = request.form['message']
    message = list(message.lower())
    send_to_bridge(message)
    return render_template('finish.html', message=message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080' )