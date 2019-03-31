from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

user1 = User(name="Reema", email="reemast93@gmail.com",
             picture='https://upload.wikimedia.org/wikipedia/commons/0/02/Circle-icons-computer.svg')
session.add(user1)
session.commit()

category1 = Category(name="Documentaries", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(
    name="7 Days Out",
    user_id=1,
    description="Witness the excitement and drama behind the scenes "
    "in the seven days leading up to major live events in the worlds "
    "of sports, fashion, space and food.",
    category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="Ask the Doctor",
    user_id=1,
    description="From allergies to diet to sleep, "
    "three friendly doctors share expert advice, "
    "bust medical myths and test the latest treatments.",
    category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(
    name="Chef's Table",
    user_id=1,
    description="In this Emmy-nominated series, "
    "meet culinary stars around the world who are "
    "redefining gourmet food with innovative dishes "
    "and tantalizing desserts.",
    category=category1)

session.add(item3)
session.commit()

category2 = Category(name="Dramas", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(
    name="Battle",
    user_id=1,
    description="After Amalie's dad goes bankrupt, "
    "the young dancer's affluent life collapses. "
    "But she finds a new beat to follow after meeting "
    "hip-hop dancer Mikael.",
    category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(
    name="Benji",
    user_id=1,
    description="A determined dog comes to the rescue "
    "and helps heal a broken family when a young boy "
    "and his sister stumble into some serious danger.",
    category=category2)

session.add(item2)
session.commit()

category3 = Category(name="Animation", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(
    name="The Boss Baby",
    user_id=1,
    description="The Boss Baby brings his big brother "
    "Tim to the office to teach him the art of business "
    "in this animated series sprung from the hit film.",
    category=category3)

session.add(item1)
session.commit()

categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
