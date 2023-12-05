# Spotify Data Modeling Project

## OVERVIEW

This project involves extracting spotify dataset using Spotipy Python Library, creating all conceptual, logical and physical models, and loading the data into PostgreSQL database.

Entities - Category, Playlist, Track, Artist, Album
Junction Entities - Category_Playlist, Playlist_Track, Artist_Track, Artist_Album

## Steps taken for Project
1. Setting up Spotify Developers Account to get CLIENT_ID and CLIENT_SECRET
2. Install Python library and explore APIs : pip3 install spotipy
3. Create Data Models : Conceptual, Logical and Physical Models
4. Transform extracted result for inserting into tables i.e, remove incomplete or duplicate records, etc.
5. Create Postgres database Connection, Create tables and Insert Records.

## Folder Structure
1. spotify_datasource.py - Extract Spotify data into CSVs
2. transform_data.py - Transform dataset to insert into tables
3. load_postgres.py - Connect with local Postgres database and Insert data into created tables.
4. spotify_data/ - Raw data extracted from spotipy library
5. data/ - Final processed data to insert into tables
6. models/ - Images of data model designss

## Tech Stack
1. Python 3.x
2. PostgreSQL
3. Spotipy Library


### RESOURCES -
1. https://medium.com/@maxtingle/getting-started-with-spotifys-api-spotipy-197c3dc6353b
2. https://developer.spotify.com/documentation/web-api 
3. https://spotipy.readthedocs.io 

