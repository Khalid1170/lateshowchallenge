from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lateshow.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return {"message": "Welcome to the Late Show API"}

# GET /episodes
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    episodes_list = [episode.to_dict() for episode in episodes]
    return jsonify(episodes_list), 200

# GET /episodes/:id
@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict()), 200
    return jsonify({"error": "Episode not found"}), 404

# GET /guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    guests_list = [guest.to_dict() for guest in guests]
    return jsonify(guests_list), 200

# POST /appearances
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()

    try:
        rating = data.get("rating")
        episode_id = data.get("episode_id")
        guest_id = data.get("guest_id")

        # Validate required fields
        if not all([rating, episode_id, guest_id]):
            return jsonify({"errors": ["Missing required fields"]}), 400

        # Create and validate new appearance
        new_appearance = Appearance(
            rating=rating,
            episode_id=episode_id,
            guest_id=guest_id
        )

        db.session.add(new_appearance)
        db.session.commit()

        return jsonify(new_appearance.to_dict()), 201

    except ValueError as ve:
        return jsonify({"errors": [str(ve)]}), 400
    except Exception as e:
        return jsonify({"errors": ["An error occurred while creating the appearance"]}), 500

if __name__ == "__main__":
    app.run(debug=True)
