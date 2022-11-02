from django.views.decorators.http import require_http_methods


# from django.http import JsonResponse
# import requests
# import os

# from oauthlib.oauth2 import BackendApplicationClient
# from requests_oauthlib import OAuth2Session


#> create search encoder
#   ?? artists.items.genres/id/images.url/name/uri
#> create top tracks encoder
#   ?? tracks.duration_ms/id/name/preview_url/track_number/uri

@require_http_methods(["GET"])
def toptracks(request):
    pass
    #> define request
    #   Input -> request: artist name
    #      - Use Spotify Search API for artist ID
    #          -> GET https://api.spotify.com/v1/search
    #               Params: artist name && type = artist && limit = 1
    #          -> search encoder
    #          -> return artist ID
    #      - Use Spotify Artist / Top Tracks API for tracks
    #          -> GET  https://api.spotify.com/v1/artists/{id}/top-tracks
    #              Params: artist ID // market = us
    #          -> top tracks encoder
    #          -> return top tracks
    #    Output -> artist's top 10 track details



# @require_http_methods(["GET", "POST"])
# def toptracks_list(request):
#     # Setup oauth
#     client_id = os.environ["SPOTIFY_CLIENT_ID"]
#     client_secret = ["SPOTIFY_CLIENT_SECRET"]
#     token_url = "https://accounts.spotify.com/api/token"

#     client = BackendApplicationClient(client_id=client_id)
#     oauth = OAuth2Session(client=client)
#     token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)

#     # API URL
#     api_url = "https://api.spotify.com/v1"

#     artist_id = '144HzhpLjcR9k37w5Ico9B'
#     # Use artist ID to get top tracks
#     top_tracks_url = f"{api_url}/artists/{artist_id}/top-tracks?market=ES"
#     top_tracks_response = oauth.get(top_tracks_url).json()
#     tracks = top_tracks_response['tracks']
#     return JsonRsponse({'tracks': tracks})