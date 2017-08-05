from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Base, GameItem, User

engine = create_engine('sqlite:///gamecatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Game for Action
genre1 = Genre(user_id=1, name="Action")

session.add(genre1)
session.commit()


# Game for Adventure
genre2 = Genre(user_id=1, name="Adventure")

session.add(genre2)
session.commit()


# Game for Role Playing
genre1 = Genre(user_id=1, name="Role-playing")

session.add(genre1)
session.commit()

gameItem1 = GameItem(user_id=1, name="World of WarCraft", description="massively multiplayer online role-playing game - MMORPG", release_year="2004", platform="PC", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Fire Emblem Heroes", description="Fire Emblem Heroes is a free-to-play tactical role-playing game developed by Intelligent Systems and Nintendo for iOS and Android devices. The game is a mobile spin-off of the Fire Emblem series", release_year="2017", platform="Mobile", genre=genre1)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="Diablo", description="action role-playing hack and slash video game developed by Blizzard North and released by Blizzard Entertainment", release_year="1997", platform="PC", genre=genre1)

session.add(gameItem3)
session.commit()

gameItem4 = GameItem(user_id=1, name="Paper Mario", description="Paper Mario's gameplay is a blend of traditional Japanese role-playing games and Mario-esque platforming features; Mario has the ability to jump in both the overworld and in battle, and jumping remains one of the most important actions in the game. ", release_year="2001", platform="Game Console", genre=genre1)

session.add(gameItem4)
session.commit()


# Game for Strategy
genre1 = Genre(user_id=1, name="Strategy")

session.add(genre1)
session.commit()


gameItem1 = GameItem(user_id=1, name="Warcraft III", description="High fantasy real-time strategy video game developed and published by Blizzard Entertainment. ",
 release_year="2002", platform="PC", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="StarCraft", description="StarCraft is a military science fiction media franchise created by Chris Metzen and James Phinney, and owned by Blizzard Entertainment.", release_year="1998", platform="PC", genre=genre1)

session.add(gameItem2)
session.commit()


# Game for Simulation
genre1 = Genre(user_id=1, name="Simulation")

session.add(genre1)
session.commit()


# Game for Sports
genre1 = Genre(user_id=1, name="Sports")

session.add(genre1)
session.commit()


# Game for Action Adventure
genre1 = Genre(user_id=1, name="Action Adventure")

session.add(genre1)
session.commit()


print "added game items!"
