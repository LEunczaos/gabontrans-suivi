from flask import Flask, jsonify

app = Flask(__name__)
app.json.ensure_ascii = False

COLIS = {
    "GT-1001": {"client": "SOTELGAB", "statut": "En transit", "ville": "Libreville"},
    "GT-1002": {"client": "TRANSGABON FRET", "statut": "Livré", "ville": "Port-Gentil"},
}

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

@app.route("/colis/<string:colis_id>", methods=["GET"])
def get_colis(colis_id):
    colis = COLIS.get(colis_id)
    if colis:
        return jsonify(colis), 200
    return jsonify({"error": "Colis not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
