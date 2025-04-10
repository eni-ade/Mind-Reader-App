import os
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    player_choice = int(data.get("choice"))
    computer_choice = random.randint(1, 10)

    if player_choice == computer_choice:
        result = {
            "message": f"You chose {player_choice}, computer chose {computer_choice}. You lose ☹️",
            "win": False,
        }
    else:
        result = {
            "message": f"You chose {player_choice}, computer chose {computer_choice}. You win! 😊",
            "win": True,
        }

    return jsonify(result)


# 🔥 Use this for deployment on Render:
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides a PORT env variable
    app.run(host="0.0.0.0", port=port)
