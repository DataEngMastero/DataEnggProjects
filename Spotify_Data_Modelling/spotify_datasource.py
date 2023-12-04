import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import pandas as pd
import random
import json

client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET

# Setup Spotify Client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_categories(spotify):
    categories = spotify.categories(country='IN')
    category_list = categories['categories']['items']

    category_id_list = []
    category_name_list = []
    for category in category_list:
        category_id_list.append(category['id'])
        category_name_list.append(category['name'])
    
    category_df = pd.DataFrame({'category_id': category_id_list, 'category_name': category_name_list})
    category_df.to_csv('spotify_data/category.csv', index=False)
# get_categories(spotify)

def get_category_playlists(spotify):
    category_df = pd.read_csv('spotify_data/category.csv')
    category_id_list = []
    description_list = []
    playlist_id_list = []
    playlist_name_list = []
    tracks_count_list = []
    playlist_uri_list = []
    for category_id in category_df['category_id']:
        print(f"Executing for {category_id} = ")
        category_playlists_list = spotify.category_playlists(category_id=category_id, limit = random.randint(1,20))
        category_playlists = category_playlists_list['playlists']['items']
        
        for playlist in category_playlists:
            category_id_list.append(category_id)
            description_list.append(playlist['description'])
            playlist_id_list.append(playlist['id'])
            playlist_name_list.append(playlist['name'])
            tracks_count_list.append(playlist['tracks']['total'])
            playlist_uri_list.append(playlist['uri'])

    playlist_df = pd.DataFrame({
        'category_id': category_id_list, 
        'description': description_list,
        'playlist_id': playlist_id_list,
        'playlist_name': playlist_name_list,
        'tracks_count': tracks_count_list,
        'uri': playlist_uri_list
    })

    playlist_df.to_csv('spotify_data/playlists.csv', index=False)
# get_category_playlists(spotify)

def get_tracks_albums_artists(spotify):
    playlists_df = pd.read_csv('spotify_data/playlists.csv')

    tracks_df = pd.DataFrame()
    albums_df = pd.DataFrame()
    artists_df = pd.DataFrame()


    for playlist in playlists_df['playlist_id'].head(20):
        print(f"Executing for Playlist - {playlist}")
        tracks = spotify.playlist_tracks(playlist_id=playlist)
        tracks_list = tracks['items']

        playlist_id_list = []
        track_added_at_list = []
        track_duration_ms_list = []
        track_is_explicit_list = []
        track_id_list = []
        track_name_list = []
        track_popularity_list = []
        track_album_list = []
        track_artist_list = []
        track_uri_list = []

        album_id_list = []
        album_name_list = []
        album_release_date_list = []
        album_track_count_list = []
        album_uri_list = []
        album_type_list = []
        album_artists_names = []

        artist_id_list = []
        artist_name_list = []
        artist_uri_list = []
        artist_followers_list = []
        artist_genres_list = [] 
        artist_popularity_list = [] 

        print(f"Track List count - {len(tracks_list)}")

        for track in tracks_list:
            if track['track']:
                playlist_id_list.append(playlist)
                track_added_at_list.append(track['added_at'])
                track_details = track['track']
                track_duration_ms_list.append(track_details['duration_ms'])
                track_is_explicit_list.append(track_details['explicit'])
                track_id_list.append(track_details['id'])
                track_name_list.append(track_details['name'])
                track_popularity_list.append(track_details['popularity'])
                track_uri_list.append(track_details['uri'])
                track_album_list.append(track_details['album']['id'])
                # track_artist_list

                album_details = track_details['album']
                album_id_list.append(album_details['id'])
                album_name_list.append(album_details['name'])
                album_release_date_list.append(album_details['release_date'])
                album_track_count_list.append(album_details['total_tracks'])
                album_uri_list.append(album_details['uri'])
                album_type_list.append(album_details['album_type'])
                # album_artists_names

                artists_list = []
                artists_detials = track_details['artists']
                print(f"Artists List count - {len(artists_detials)}")

                for artist in artists_detials:
                    artist_id_list.append(artist['id'])
                    artists_list.append(artist['id'])
                    artist_name_list.append(artist['name'])
                    artist_uri_list.append(artist['uri'])

                    artist_detail = spotify.artist(artist['id'])
                    artist_followers_list.append(artist_detail['followers']['total'])
                    artist_genres_list.append(artist_detail['genres'])
                    artist_popularity_list.append(artist_detail['popularity'])

                track_artist_list.append(artists_list)
                album_artists_names.append(artists_list)


        tracks_df_temp = pd.DataFrame({
            'track_id': track_id_list, 
            'track_name': track_name_list,
            'popularity': track_popularity_list,
            'explicit': track_is_explicit_list,
            'duration_ms': track_duration_ms_list,
            'added_at': track_added_at_list,
            'playlist_id': playlist_id_list,
            'uri': track_uri_list,
            'artists': album_artists_names,
            'album_id': track_album_list
        })
        tracks_df = pd.concat([tracks_df, tracks_df_temp])

        albums_df_temp = pd.DataFrame({
            'album_id': album_id_list,
            'album_name': album_name_list,
            'release_date': album_release_date_list,
            'tracks_count': album_track_count_list,
            'uri': album_uri_list,
            'album_type': album_type_list,
            'artists': album_artists_names

        })
        albums_df = pd.concat([albums_df, albums_df_temp])

        artists_df_temp = pd.DataFrame({
            'artist_id': artist_id_list,
            'artist_name': artist_name_list,
            'uri': artist_uri_list,
            'followers': artist_followers_list,
            'popularity': artist_popularity_list,
            'genres': artist_genres_list
        })
        artists_df = pd.concat([artists_df, artists_df_temp])

    tracks_df.to_csv('spotify_data/tracks.csv', index=False)
    albums_df.to_csv('spotify_data/albums.csv', index=False)
    artists_df.to_csv('spotify_data/artists.csv', index=False)
get_tracks_albums_artists(spotify)


