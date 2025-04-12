from models import db, Episode, Guest, Appearance
from app import app

with app.app_context():
    print("🌱 Seeding database...")

    db.drop_all()
    db.create_all()

    # Add Episodes
    ep1 = Episode(date="3/01/00", number=201)
    ep2 = Episode(date="3/02/00", number=202)
    ep3 = Episode(date="3/03/00", number=203)

    db.session.add_all([ep1, ep2, ep3])

    # Add Guests
    g1 = Guest(name="Elon Musk", occupation="Tech Entrepreneur")
    g2 = Guest(name="Robert Downey Jr.", occupation="Actor")
    g3 = Guest(name="Will Smith", occupation="Actor/Musician")
    g4 = Guest(name="Michael Blackson", occupation="Comedian")

    db.session.add_all([g1, g2, g3, g4])
    db.session.commit()

    # Add Appearances
    a1 = Appearance(rating=5, episode_id=ep1.id, guest_id=g1.id)
    a2 = Appearance(rating=4, episode_id=ep2.id, guest_id=g2.id)
    a3 = Appearance(rating=3, episode_id=ep2.id, guest_id=g3.id)
    a4 = Appearance(rating=5, episode_id=ep3.id, guest_id=g4.id)

    db.session.add_all([a1, a2, a3, a4])
    db.session.commit()

    print("✅ Done seeding!")
