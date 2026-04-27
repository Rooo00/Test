from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suma')
def suma():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify(resultado=a + b)
    except (TypeError, ValueError):
        return jsonify(error="'a' y 'b' deben ser números"), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)