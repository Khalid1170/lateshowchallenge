Got it! Here's the updated README with the correct project name and all required endpoints included:

````markdown
# 📺 Late Show API

Welcome to the Late Show API! This Flask application is designed to manage episodes, guests, and appearances for a fictional late-night show.

## 🚀 Project Setup

### Requirements

- Python 3.11
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Postman (for testing API requests)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/lateshow-yourname.git
cd lateshow-yourname
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up the database**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. **Seed the database**

```bash
python seed.py
```

6. **Run the application**

```bash
flask run
```

---

## 🛠 Endpoints

### GET `/episodes`

Returns a list of all episodes with their appearances and guest details.

#### Response Example

```json
[
  {
    "id": 1,
    "date": "3/01/00",
    "number": 201,
    "appearances": [
      {
        "id": 1,
        "rating": 5,
        "guest_id": 1,
        "episode_id": 1,
        "guest": {
          "id": 1,
          "name": "Elon Musk",
          "occupation": "Tech Entrepreneur"
        },
        "episode": {
          "id": 1,
          "date": "3/01/00",
          "number": 201
        }
      }
    ]
  }
]
```

---

### GET `/episodes/<int:id>`

Returns a single episode and its appearances with guest info.

#### Successful Response

```json
{
  "id": 1,
  "date": "3/01/00",
  "number": 201,
  "appearances": [ ... ]
}
```

#### Error Response

```json
{
  "error": "Episode not found"
}
```

---

### GET `/guests`

Returns a list of all guests.

#### Response Example

```json
[
  {
    "id": 1,
    "name": "Elon Musk",
    "occupation": "Tech Entrepreneur"
  },
  ...
]
```

---

### POST `/appearances`

Creates a new appearance record. You must supply a `rating` between 1 and 5, and valid `episode_id` and `guest_id`.

#### Request Example

```json
{
  "rating": 5,
  "episode_id": 1,
  "guest_id": 2
}
```

#### Success Response

```json
{
  "id": 5,
  "rating": 5,
  "guest_id": 2,
  "episode_id": 1,
  "episode": {
    "id": 1,
    "date": "3/01/00",
    "number": 201
  },
  "guest": {
    "id": 2,
    "name": "Robert Downey Jr.",
    "occupation": "Actor"
  }
}
```

#### Validation Error Response

```json
{
  "errors": ["Rating must be between 1 and 5."]
}
```

---

## 🔧 Dev Notes

- All relationships are set up with cascading deletes.
- Validations are in place to ensure `rating` is between 1 and 5.
- Seed file uses custom guest names and episodes.

---


---
```