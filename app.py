from flask import Flask, jsonify, request
from game import TicTacToe

app = Flask(__name__)
game = TicTacToe()

@app.route("/")
def home():
    return "TicTacToe DevOps App Running"

@app.route("/board")
def board():
    return jsonify(game.get_board())

@app.route("/move", methods=["POST"])
def move():
    data = request.json
    position = data.get("position")

    if game.make_move(position):
        return jsonify({"status": "success", "board": game.get_board()})
    return jsonify({"status": "invalid"}), 400

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
