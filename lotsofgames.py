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

# Game for UrbanBurger
genre1 = Genre(user_id=1, name="Urban Burger")

session.add(genre1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.50", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()


gameItem1 = GameItem(user_id=1, name="French Fries", description="with garlic and parmesan",
                     price="$2.99", platform="Appetizer", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="$5.50", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", platform="Dessert", genre=genre1)

session.add(gameItem3)
session.commit()

gameItem4 = GameItem(user_id=1, name="Sirloin Burger", description="Made with grade A beef",
                     price="$7.99", platform="Entree", genre=genre1)

session.add(gameItem4)
session.commit()

gameItem5 = GameItem(user_id=1, name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", platform="Beverage", genre=genre1)

session.add(gameItem5)
session.commit()

gameItem6 = GameItem(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", platform="Beverage", genre=genre1)

session.add(gameItem6)
session.commit()

gameItem7 = GameItem(user_id=1, name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese", price="$3.49", platform="Entree", genre=genre1)

session.add(gameItem7)
session.commit()

gameItem8 = GameItem(user_id=1, name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
                     price="$5.99", platform="Entree", genre=genre1)

session.add(gameItem8)
session.commit()


# Game for Super Stir Fry
genre2 = Genre(user_id=1, name="Super Stir Fry")

session.add(genre2)
session.commit()


gameItem1 = GameItem(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     price="$7.99", platform="Entree", genre=genre2)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Peking Duck",
                     description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="$25", platform="Entree", genre=genre2)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     price="15", platform="Entree", genre=genre2)

session.add(gameItem3)
session.commit()

gameItem4 = GameItem(user_id=1, name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", platform="Entree", genre=genre2)

session.add(gameItem4)
session.commit()

gameItem5 = GameItem(user_id=1, name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", platform="Entree", genre=genre2)

session.add(gameItem5)
session.commit()

gameItem6 = GameItem(user_id=1, name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     price="12", platform="Entree", genre=genre2)

session.add(gameItem6)
session.commit()


# Game for Panda Garden
genre1 = Genre(user_id=1, name="Panda Garden")

session.add(genre1)
session.commit()


gameItem1 = GameItem(user_id=1, name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     price="$8.99", platform="Entree", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     price="$6.99", platform="Appetizer", genre=genre1)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="Gyoza", description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
                     price="$9.95", platform="Entree", genre=genre1)

session.add(gameItem3)
session.commit()

gameItem4 = GameItem(user_id=1, name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$6.99", platform="Entree", genre=genre1)

session.add(gameItem4)
session.commit()

gameItem2 = GameItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()


# Game for Thyme for that
genre1 = Genre(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(genre1)
session.commit()


gameItem1 = GameItem(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="$2.99", platform="Dessert", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="$5.99", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="Honey Boba Shaved Snow",
                     description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price="$4.50", platform="Dessert", genre=genre1)

session.add(gameItem3)
session.commit()

gameItem4 = GameItem(user_id=1, name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="$6.95", platform="Appetizer", genre=genre1)

session.add(gameItem4)
session.commit()

gameItem5 = GameItem(user_id=1, name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="$7.95", platform="Entree", genre=genre1)

session.add(gameItem5)
session.commit()

gameItem2 = GameItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$6.80", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()


# Game for Tony's Bistro
genre1 = Genre(user_id=1, name="Tony\'s Bistro ")

session.add(genre1)
session.commit()


gameItem1 = GameItem(user_id=1, name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="$13.95", platform="Entree", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
                     price="$4.95", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", platform="Entree", genre=genre1)

session.add(gameItem3)
session.commit()

gameItem4 = GameItem(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", platform="Dessert", genre=genre1)

session.add(gameItem4)
session.commit()

gameItem5 = GameItem(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="$7.95", platform="Entree", genre=genre1)

session.add(gameItem5)
session.commit()


# Game for Andala's
genre1 = Genre(user_id=1, name="Andala\'s")

session.add(genre1)
session.commit()


gameItem1 = GameItem(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="$9.95", platform="Entree", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="$7.95", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="$6.50", platform="Appetizer", genre=genre1)

session.add(gameItem3)
session.commit()

gameItem4 = GameItem(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="$6.75", platform="Appetizer", genre=genre1)

session.add(gameItem4)
session.commit()

gameItem2 = GameItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$7.00", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()


# Game for Auntie Ann's
genre1 = Genre(user_id=1, name="Auntie Ann\'s Diner' ")

session.add(genre1)
session.commit()

gameItem9 = GameItem(user_id=1, name="Chicken Fried Steak",
                     description="Fresh battered sirloin steak fried and smothered with cream gravy", price="$8.99", platform="Entree", genre=genre1)

session.add(gameItem9)
session.commit()


gameItem1 = GameItem(user_id=1, name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
                     price="$2.99", platform="Dessert", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="$10.95", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()

gameItem3 = GameItem(user_id=1, name="Morels on toast (seasonal)",
                     description="Wild morel mushrooms fried in butter, served on herbed toast slices", price="$7.50", platform="Appetizer", genre=genre1)

session.add(gameItem3)
session.commit()

gameItem4 = GameItem(user_id=1, name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.",
                     price="$8.95", platform="Entree", genre=genre1)

session.add(gameItem4)
session.commit()

gameItem2 = GameItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="$9.50", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()

gameItem10 = GameItem(user_id=1, name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="$1.99", platform="Dessert", genre=genre1)

session.add(gameItem10)
session.commit()


# Game for Cocina Y Amor
genre1 = Genre(user_id=1, name="Cocina Y Amor ")

session.add(genre1)
session.commit()


gameItem1 = GameItem(user_id=1, name="Super Burrito Al Pastor",
                     description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", price="$5.95", platform="Entree", genre=genre1)

session.add(gameItem1)
session.commit()

gameItem2 = GameItem(user_id=1, name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="$7.99", platform="Entree", genre=genre1)

session.add(gameItem2)
session.commit()


genre1 = Genre(user_id=1, name="State Bird Provisions")
session.add(genre1)
session.commit()

gameItem1 = GameItem(user_id=1, name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="$5.95", platform="Appetizer", genre=genre1)

session.add(gameItem1)
session.commit

gameItem1 = GameItem(user_id=1, name="Guanciale Chawanmushi",
                     description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)", price="$6.95", platform="Dessert", genre=genre1)

session.add(gameItem1)
session.commit()


gameItem1 = GameItem(user_id=1, name="Lemon Curd Ice Cream Sandwich",
                     description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", price="$4.25", platform="Dessert", genre=genre1)

session.add(gameItem1)
session.commit()


print "added game items!"
