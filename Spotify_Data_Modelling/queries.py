create_queries = {
    
    # category_id,category_name
    "category_create_qry" : """ 
        CREATE TABLE IF NOT EXISTS category (
            category_id VARCHAR PRIMARY KEY NOT NULL,
            category_name VARCHAR
        );
    """,
    
    # playlist_id,playlist_name,description,tracks_count,uri
    "playlist_create_qry" : """
        CREATE TABLE IF NOT EXISTS playlist (
            playlist_id VARCHAR PRIMARY KEY NOT NULL,
            playlist_name VARCHAR,
            description VARCHAR,
            tracks_count NUMERIC,
            uri VARCHAR UNIQUE NOT NULL
        );
    """,

    # track_id,track_name,popularity,explicit,duration_ms,added_at,album_id
    "track_create_qry" : """
        CREATE TABLE IF NOT EXISTS track (
            track_id VARCHAR PRIMARY KEY NOT NULL,
            track_name VARCHAR,
            popularity NUMERIC,
            explicit BOOLEAN,
            duration_ms NUMERIC,
            added_at TIMESTAMP,
            album_id VARCHAR,
            FOREIGN KEY (album_id) REFERENCES album(album_id)
        );
    """,

    # album_id,album_name,release_date,tracks_count,uri,album_type
    "album_create_qry" : """
        CREATE TABLE IF NOT EXISTS album (
            album_id VARCHAR PRIMARY KEY NOT NULL,
            album_name VARCHAR,
            release_date DATE,
            tracks_count NUMERIC,
            uri VARCHAR UNIQUE NOT NULL,
            album_type VARCHAR
        );
    """,

    # artist_id,artist_name,uri,followers,popularity,genres
    "artist_create_qry" : """ 
        CREATE TABLE IF NOT EXISTS artist (
            artist_id VARCHAR PRIMARY KEY NOT NULL,
            artist_name VARCHAR,
            uri VARCHAR UNIQUE NOT NULL,
            followers NUMERIC,
            popularity NUMERIC,
            genres VARCHAR[]
        );
    """,

    # artists,album_id
    "artist_album_create_qry" : """
        CREATE TABLE IF NOT EXISTS artist_album (
            artist_id VARCHAR,
            album_id VARCHAR,
            FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
            FOREIGN KEY (album_id) REFERENCES album(album_id),
            PRIMARY KEY (artist_id, album_id)
        );
    """,

    # artists,track_id
    "artist_track_create_qry" : """ 
        CREATE TABLE IF NOT EXISTS artist_track (
            artist_id VARCHAR,
            track_id VARCHAR,
            FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
            FOREIGN KEY (track_id) REFERENCES track(track_id),
            PRIMARY KEY (artist_id, track_id)
        );
    """,
   
    # category_id,playlist_id
    "category_playlist_create_qry" : """
        CREATE TABLE IF NOT EXISTS category_playlist (
            category_id VARCHAR,
            playlist_id VARCHAR,
            FOREIGN KEY (category_id) REFERENCES category(category_id),
            FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id),
            PRIMARY KEY (category_id, playlist_id)
        );
    """,
    
    # playlist_id,track_id
    "playlist_track_create_qry" : """
        CREATE TABLE IF NOT EXISTS playlist_track (
            playlist_id VARCHAR,
            track_id VARCHAR,
            FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id),
            FOREIGN KEY (track_id) REFERENCES track(track_id),
            PRIMARY KEY (playlist_id, track_id)
        );
    """
}

insert_queries = {
    "category" : "INSERT INTO category (category_id, category_name) VALUES (%s, %s);",
    "playlist" : "INSERT INTO playlist (playlist_id, playlist_name, description, tracks_count, uri) VALUES (%s, %s, %s, %s, %s);",
    "track" : "INSERT INTO track (track_id, track_name, popularity, explicit, duration_ms, added_at, album_id) VALUES (%s, %s, %s, %s, %s, %s, %s);",
    "album" : "INSERT INTO album (album_id, album_name, release_date, tracks_count, uri, album_type)  VALUES (%s, %s, %s, %s, %s, %s);",
    "artist" : "INSERT INTO artist (artist_id, artist_name, uri, followers, popularity, genres) VALUES (%s, %s, %s, %s, %s, %s);",
    "artist_album" : "INSERT INTO artist_album (artist_id, album_id) VALUES (%s, %s);",
    "artist_track" : "INSERT INTO artist_track (artist_id, track_id) VALUES (%s, %s);",
    "category_playlist" : "INSERT INTO category_playlist (category_id, playlist_id) VALUES (%s, %s);",
    "playlist_track" : "INSERT INTO playlist_track (playlist_id, track_id) VALUES (%s, %s);"
}