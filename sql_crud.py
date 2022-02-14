"""
CRUD
"""
# we are gong to use ORM methods for these lessons
# copy the initial setup from sql_orm.py

from sqlalchemy import (
    create_engine, Column, Integer, String
)
# we don't need to import Table clase because with ORM we're
# not going to create tables, but instead we#ll be creating
# Python classes

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# sessionmaker - instead of making a connection to the database
# directly, we'll be asking for a session

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-base model for the "Programmer" table
class Programmer(base):
    """
    Programmer table
    """
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmakes,then point to our engine( the db)
Session = sessionmaker(db)

# opens an actual session by clling the Session() subclass defined above
session = Session()

# crating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margeret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

iris_smok = Programmer(
    first_name="Iris",
    last_name="Smok",
    gender="F",
    nationality="Croatian",
    famous_for="Programming"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# # this will create a second record for her
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margeret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(iris_smok)

# commit our session to the database
# session.commit()

# updating a single record
# programmer = session.query(Programmer).filter_by(id=4).first()
# since we only want one specific record, it's important to add the
# .first() method at the end of the query
# if you don't add the first() then you'll have to use a for-loop
# to iterate over the query list
# programmer.famous_for = "Mcrosoft"


# # updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()
#     # we need to commit each update within this loop

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(
#     first_name=fname, last_name=lname).first()
# #defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " "
#    + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")


# query the database to find all Programmers
programmers = session.query(Programmer)
# # for-loop to query the database
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
