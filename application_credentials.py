"""application_credentials platform the Frank HA integration."""

from homeassistant.components.application_credentials import AuthorizationServer
from homeassistant.core import HomeAssistant

# TODO Update with your own urls
OAUTH2_AUTHORIZE = "https://auth.energyonline.co.nz/auth.energyonline.co.nz/oauth2/v2.0/authorize?p=b2c_1a_signin"
OAUTH2_TOKEN = "https://auth.energyonline.co.nz/auth.energyonline.co.nz/oauth2/v2.0/token?p=b2c_1a_signin"


async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer:
    """Return authorization server."""
    return AuthorizationServer(
        authorize_url=OAUTH2_AUTHORIZE,
        token_url=OAUTH2_TOKEN,
    )
