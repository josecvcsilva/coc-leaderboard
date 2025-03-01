from urllib.parse import quote

from CoC.settings import PORTUGAL_1128_CLAN_TAG, COC_API_KEY
import requests

COC_URL = "https://api.clashofclans.com/v1"
HEADERS = {
        "Authorization": f"Bearer {COC_API_KEY}",
        "Accept": "application/json"
    }
def make_request():
    url = f"{COC_URL}/clans/{PORTUGAL_1128_CLAN_TAG}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def get_players(clan_tag: str = PORTUGAL_1128_CLAN_TAG):
    enc_clan_tag = quote(clan_tag)
    url = f"{COC_URL}/clans/{enc_clan_tag}/members"
    response = requests.get(url, headers=HEADERS, params={"limit": 50})
    return response
