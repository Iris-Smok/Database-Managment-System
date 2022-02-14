"""
ORM
"""
from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
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


# create a class-based model from "Artist" table
class Artist(base):
    """
    Artist
    """
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


# create a class_base model from the "Album" table
class Album(base):

    """
    Album
    """
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


# create a class-base model from the "Track" table
class Track(base):
    """
    Track
    """
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmakes,then point to our engine( the db)
Session = sessionmaker(db)

# opens an actual session by clling the Session() subclass defined above
session = Session()

# crating the database using declarative_base subclass
base.metadata.create_all(db)


# Query 1 - select all records from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep=" | ")


# Query 2 - select only the "Name" column from the "Artist" table
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.Name, sep=" | ")


# Query 3 - select only "Queen" from the "Artist" table
# we know that we only want to find a single artist, the new variable
# is artist singular, we can use .filter_by() method
# and using the Name column, we'll specify "Qeen"
# since it should technically only return one record, we can
# use the .first() method to only gives us the first item
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# same result but having filtered by the ID instead of the Name
# artist = session.query(Artist).filter_by(ArtistId="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")


# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#     print(album.AlbumId, album.Title, album.ArtistId, sep=" | ")


# Query 6 - select all tracks where the composer is "Queen" from the
# "Track" table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | ")
