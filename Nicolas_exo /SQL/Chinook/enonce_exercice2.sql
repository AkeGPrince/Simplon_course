USE Chinook;

-- Exercise 1
-- QUERY 1: Explore PlaylistTrack (line count : 8715)

-- QUERY 2: How many track does each playlist have? Order from largest to smallest playlists. (line count : 14)
SELECT  PlaylistId, COUNT(PlaylistId) AS number
FROM playlist_track
GROUP BY PlaylistId
ORDER BY number DESC
-- QUERY 3: Is there a difference between the unit price contained in invoice_items and tracks ?
SELECT *
FROM invoice_items
JOIN tracks ON tracks.TrackId = invoice_items.TrackId
WHERE tracks.UnitPrice != invoice_items.UnitPrice

-- QUERY 4: Identify the rows where either TrackId or PlaylistId is NULL (PlaylistTrack table).
SELECT *
FROM playlist_track
WHERE TrackId IS NULL OR PlaylistId IS NULL
-- QUERY 5: Group the songs according to the different types of media (use a count) (line count : 5)
SELECT media_types.name as types, COUNT(tracks.name) as nombre
FROM media_types
JOIN tracks ON media_types.MediaTypeId = tracks.MediaTypeId
GROUP BY types
-- QUERY 6: Show the number of tracks for each playlist that have more than 100 tracks. (line count : ())
SELECT  PlaylistId, COUNT(PlaylistId) AS number
FROM playlist_track
GROUP BY PlaylistId
HAVING number > 100
ORDER BY number DESC
-- QUERY 7: Show the number of tracks for each playlist with an even PlaylistId that have more than 100 tracks. (line count : 2)
SELECT  PlaylistId, COUNT(PlaylistId) AS number
FROM playlist_track
GROUP BY PlaylistId
HAVING number > 100 AND number % 2 = 0
-- QUERY 8: Join table PlaylistTrack with Playlist (line count : 8715)
SELECT *
FROM playlist_track
JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
-- QUERY 9: Join table PlaylistTrack with Playlist without any column duplicate (line count : 8715)
SELECT TrackId, Name
FROM playlist_track
JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
-- QUERY 10: Join table PlaylistTrack with Playlist without any column duplicate and using aliases in your code (AS) (line count : 8715)

-- QUERY 11: How many track does each playlist have? Show the name of the playlist in your result. (line count : 14)
SELECT playlists.Name ,COUNT(playlist_track.TrackId) as nombre
FROM playlist_track
JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
GROUP BY playlists.PlaylistId
-- QUERY 12: Are they albums title whose names are similar to playlists name ?
SELECT COUNT(playlists.name )as similarities
FROM albums
JOIN tracks ON albums.AlbumId = tracks.AlbumId
JOIN playlist_track ON playlist_track.TrackId = tracks.TrackId
JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
WHERE playlists.name = albums.Title
-- QUERY 13: Count the number of albums for each genre. Order the results by most to least popular genre. (line count : 25)
SELECT genres.name, COUNT(albums.Title)
FROM genres
JOIN tracks ON genres.GenreId = tracks.GenreId
JOIN albums ON tracks.AlbumId = albums.AlbumId
GROUP BY genres.name

-- QUERY 14: Show the same result and add the name of the genre. (line count : 25)
SELECT genres.name as genre , COUNT(albums.Title) as number_of_albums
FROM genres
JOIN tracks ON genres.GenreId = tracks.GenreId
JOIN albums ON tracks.AlbumId = albums.AlbumId
GROUP BY genres.name
-- QUERY 15: Count the number of playlists for each genre. Order the results by most to least popular genre. (line count : 25)
SELECT genres.name, COUNT(playlists.PlaylistId) as number_of_playlist
FROM genres
JOIN tracks ON tracks.GenreId = genres.GenreId
JOIN playlist_track ON playlist_track.TrackId = tracks.TrackId
JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
GROUP BY genres.Name
ORDER BY number_of_playlist

-- QUERY 16: How many different media, genre, tracks, albums and artists are there in this DB (1 request) ?
SELECT COUNT(media_types.name)AS number, "media " AS infos FROM media_types
UNION
SELECT COUNT(artists.name), "artist "  AS artist FROM artists
UNION
SELECT COUNT(albums.Title), "album "  AS album FROM albums
UNION
SELECT COUNT(genres.name), "genre "  AS genre FROM genres
UNION
SELECT COUNT(tracks.Name), "track " AS track FROM tracks
-- QUERY 17: Which playlist or playlists have no tracks? (line count : 4)
