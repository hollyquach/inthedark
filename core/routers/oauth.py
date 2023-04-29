import os 
from fastapi import APIRouter, Response, Request
from fastapi.responses import RedirectResponse
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

router = APIRouter()


#> set env. variables
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = f"{os.getenv('CORE_URI')}/callback"

#> Spotify API - OAuth endpoints
# REF https://developer.spotify.com/documentation/general/guides/authorization/code-flow/
spotify_auth_url = "https://accounts.spotify.com/authorize"
spotify_token_url = "https://accounts.spotify.com/api/token"


# [] review & update scopes req.
# REF https://developer.spotify.com/documentation/general/guides/authorization/scopes/
scope = [
    "user-read-email",
    "playlist-read-collaborative"
]


spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

#>> request user auth -> redirect URI
@router.get("/login")
async def user_auth_redirect(response: Response):
    authorization_url, state = spotify.authorization_url(spotify_auth_url)
    response = RedirectResponse(url= authorization_url)
    return response

#>> user auth callback & get user token
@router.get("/callback")
def callback(request: Request, response: Response):
    code = request.query_params.get('code')
    state = request.query_params.get('state')

    print(f'💬💬  >>> {code} // {state}')

    # [] request access / bearer token
    # auth = HTTPBasicAuth(client_id, client_secret)
    # token = spotify.fetch_token(spotify_token_url, auth=auth, authorization_response=redirect_response)

    # [] set up Sessions to store access & refresh token per user