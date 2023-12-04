import pandas as  pd 


def drop_duplicates(file, selected_columns, final_filename, column_in_array = None):
    actual_df = pd.read_csv(file)
    actual_df = actual_df[selected_columns]

    if column_in_array:
        actual_df[column_in_array] = actual_df[column_in_array].apply(eval)
        actual_df = actual_df.explode(column_in_array)

    actual_df = actual_df.drop_duplicates()
    
    actual_df.to_csv(final_filename, index=False)

 
# Category - No Change Required

# Category - Playlist CSV
drop_duplicates('spotify_data/playlists.csv', ['category_id', 'playlist_id'], 'data/category_playlist.csv')

# Playlist CSV
drop_duplicates('spotify_data/playlists.csv', ['playlist_id', 'playlist_name', 'description', 'tracks_count', 'uri'], 'data/playlist.csv')

# Playlist - Track CSV
drop_duplicates('spotify_data/tracks.csv', ['playlist_id', 'track_id' ], 'data/playlist_track.csv')

# Track CSV
drop_duplicates('spotify_data/tracks.csv', ['track_id', 'track_name', 'popularity', 'explicit', 'duration_ms', 'added_at', 'album_id'], 'data/track.csv')

# Album CSV
drop_duplicates('spotify_data/albums.csv', ['album_id', 'album_name', 'release_date', 'tracks_count', 'uri', 'album_type'], 'data/album.csv')

# Artist CSV
drop_duplicates('spotify_data/artists.csv', ['artist_id', 'artist_name', 'uri', 'followers', 'popularity', 'genres'], 'data/artist.csv')

# Artist Track and Artist Album CSVs
drop_duplicates('spotify_data/tracks.csv', ['artists', 'track_id' ], 'data/artist_track.csv', 'artists')
drop_duplicates('spotify_data/albums.csv', ['artists', 'album_id'], 'data/artist_album.csv', 'artists')

