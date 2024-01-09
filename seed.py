from application import db
from application.models import Character

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
entry1 = Character(name="Phoebe", age=29, catch_phrase="My eyes, my eyes")

entry2 = Character(name="Urkel", age=12, catch_phrase="Did I do that?")

entry3 = Character(name="Edward Elric (FMA)", age=22, catch_phrase="Who are you calling short?")

entry4 = Character(name="Uchiha Sasuke", age=12, catch_phrase="katon goukakyuu no jutsu")

db.session.add(entry1)

db.session.add_all([entry2, entry3, entry4])

db.session.commit()
