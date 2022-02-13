"""
SQLAlchemy
"""

from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)
# to import classes

# llink our python file to Chinook database
# executing the instructions from our localhost "chinook" database

db = create_engine("postgresql:///chinook")
# assigned to variable db to represent our database
# using create_engine, we can tell it to point to our local Chinook
# database within our Postgres server

meta = MetaData(db)
# after our engine is created and connected to our database, we need
# to use the MetaData class
# MetaData class will contain a collection of our table objects


# create variable for "Artist" table
# using the Table import, wee nedd to specify the name of our table
# and provide the meta schema
# to see the columns tables = SELECT * FROM "Artist" WHERE false;

# we are defining tables as variables
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable from "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))

    # since this is the Album table It will not act as pur primary key,
    # but instead as a Foreign Key. With the ForeignKey we need to
    # tell it which table and key to point to, so in this
    # case it's artist_table

)

track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    # Media is a foreign key but we aren't defining all tables,
    # just those that we need. So we will set it to
    # primary_key=false
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


# making the connecction
# now we need to connect to the database, using the .connect()
# method and python with-statement
# this saves our connection to the database into a variable called "connection"
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()
    # define all queries into the variable, we can comment out
    # after each time it's used

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select(
    # ).with_only_columns([artist_table.c.Name])

    # Query 3 - select only "Queen" from the "Artist" table
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # Query 4 - select only by "ArtistId" #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is "Queen" from the
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    # run query using the .execute() method from our database connection
    # we stored query resolts into a variable called results
    # that whay we can iterate over each result found and print it to Terminal
    for result in results:
        print(result)
