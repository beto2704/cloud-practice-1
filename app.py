from flask import Flask, jsonify
import datetime

app = Flask(__name__)  # __name__ en lugar de _name_

@app.route('/status')
def status():
    return jsonify({
        "service": "demo-cloud",
        "version": "1.0",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    })

if __name__ == "__main__":  # __name__ y __main__
    app.run(host="0.0.0.0", port=8080)  # host con puntos, no comas
