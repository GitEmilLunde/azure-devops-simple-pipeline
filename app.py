from flask import Flask, jsonify, request

app = Flask(__name__)

# Simpel in-memory database til demo
vindmoeller = [
    {"id": 1, "navn": "Vestas 1", "MW": 1,8},
    {"id": 2, "navn": "Vestas 2", "MW": 3},
]

@app.route('/api/vindmoeller', methods=['GET'])
def hent_vindmoeller():
    return jsonify(vindmoeller)

@app.route('/api/vindmoeller/<int:id>', methods=['GET'])
def hent_vindmoeller(id):
    vindmoelle = next((p for p in vindmoeller if p["id"] == id), None)
    if vindmoelle:
        return jsonify(vindmoelle)
    return jsonify({"fejl": "Vindmølle ikke fundet"}), 404

@app.route('/api/vindmoeller', methods=['POST'])
def opret_vindmoelle():
    data = request.get_json()
    ny_vindmoelle = {
        "id": len(vindmoeller) + 1,
        "navn": data["navn"],
        "pris": data["MW"]
    }
    produkter.append(ny_vindmoelle)
    return jsonify(ny_vindmoelle), 201

if __name__ == '__main__':
    app.run(debug=True)