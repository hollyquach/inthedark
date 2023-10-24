import os 
from fastapi import APIRouter, Response, Request
from fastapi.responses import RedirectResponse
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import requests

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
auth_state = "auth_state"

spotify = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

#>> request user auth -> redirects user to allow authorization on Spotify
@router.get("/login")
async def user_auth_redirect(response: Response):
    authorization_url, state = spotify.authorization_url(spotify_auth_url)
    response = RedirectResponse(url= authorization_url)

    response.set_cookie(key=auth_state, value=state)
    #[] Set up catch for error if auth is not granted
    return response

#>> user auth callback & get access token
@router.get("/callback")
def callback(request: Request, response: Response):
    code = request.query_params.get('code')
    state = request.query_params.get('state')

    #[] Set up PKCE extension
    auth = HTTPBasicAuth(client_id, client_secret)
    
    if state != request.cookies.get(auth_state) or state == None:
        raise HTTPException(status_code=403, detail="OAuth - state mismatch")
    else:
        token = spotify.fetch_token(spotify_token_url, auth=auth, code=code)
        return token

#[] set up session/cookies to store access & refresh token per user
# NOTE Spotify token expires in 3600 aka 60 minutes
 