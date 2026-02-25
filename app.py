from flask import Flask, jsonify, request

app = Flask(__name__)

# Simpel in-memory database til demo
produkter = [
    {"id": 1, "navn": "Laptop", "pris": 9999},
    {"id": 2, "navn": "Mus", "pris": 199},
]

@app.route('/api/produkter', methods=['GET'])
def hent_produkter():
    return jsonify(produkter)

@app.route('/api/produkter/<int:id>', methods=['GET'])
def hent_produkt(id):
    produkt = next((p for p in produkter if p["id"] == id), None)
    if produkt:
        return jsonify(produkt)
    return jsonify({"fejl": "Produkt ikke fundet"}), 404

@app.route('/api/produkter', methods=['POST'])
def opret_produkt():
    data = request.get_json()
    nyt_produkt = {
        "id": len(produkter) + 1,
        "navn": data["navn"],
        "pris": data["pris"]
    }
    produkter.append(nyt_produkt)
    return jsonify(nyt_produkt), 201

if __name__ == '__main__':
    app.run(debug=True)