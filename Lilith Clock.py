from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/lilith-time')
def get_lilith_time():
    cork_time = datetime.now(pytz.timezone("Europe/Dublin"))
    return jsonify({
        "subbu_time": cork_time.strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": "Europe/Dublin",
        "source": "Subbu's Clock for Lilith"
    })

if __name__ == '__main__':
    app.run(debug=True)
