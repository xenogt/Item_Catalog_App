from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Catagory, Base, Item
 
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()


catagory1 = Catagory(name = "Urban Burger")

session.add(catagory1)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory1)

session.add(item1)
session.commit()

item2 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory1)

session.add(item2)
session.commit()

item3 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory1)

session.add(item3)
session.commit()


catagory2 = Catagory(name = "Urban Burger")

session.add(catagory2)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory2)

session.add(item1)
session.commit()

item2 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory2)

session.add(item2)
session.commit()

item3 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory2)

session.add(item3)
session.commit()


catagory3 = Catagory(name = "Urban Burger")

session.add(catagory3)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory3)

session.add(item1)
session.commit()

item2 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory3)

session.add(item2)
session.commit()

item3 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory3)

session.add(item3)
session.commit()


catagory4 = Catagory(name = "Urban Burger")

session.add(catagory4)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory4)

session.add(item1)
session.commit()

item2 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory4)

session.add(item2)
session.commit()

item3 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory4)

session.add(item3)
session.commit()


catagory5 = Catagory(name = "Urban Burger")

session.add(catagory5)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory5)

session.add(item1)
session.commit()

item2 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory5)

session.add(item2)
session.commit()

item3 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory5)

session.add(item3)
session.commit()

catagory6 = Catagory(name = "Urban Burger")

session.add(catagory6)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory6)

session.add(item1)
session.commit()

item2 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory6)

session.add(item2)
session.commit()

item3 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory6)

session.add(item3)
session.commit()


catagory7 = Catagory(name = "Urban Burger")

session.add(catagory7)
session.commit()


item1 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory7)

session.add(item1)
session.commit()

item2 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory7)

session.add(item2)
session.commit()

item3 = Item(name = "French Fries", description = "with garlic and parmesan", catagory = catagory7)

session.add(item3)
session.commit()