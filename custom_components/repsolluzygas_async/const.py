import logging
from datetime import timedelta

LOGGER = logging.getLogger(__name__)

# Dominio de la integración (debe coincidir con manifest.json y config_flow.py)
DOMAIN = "repsolluzygas_async"

# Endpoints
LOGIN_URL = "https://login.repsol.es/accounts.login"
BASE_API_URL = "https://areacliente.repsol.es/api/proxy/"
CONTRACTS_URL = f"{BASE_API_URL}houses"
HOUSES_URL = f"{BASE_API_URL}houses/{{}}"
INVOICES_URL = f"{BASE_API_URL}houses/{{}}/products/{{}}/invoices?limit=10"
COSTS_URL = f"{BASE_API_URL}houses/{{}}/products/{{}}/consumption/accumulated"
NEXT_INVOICE_URL = f"{BASE_API_URL}houses/{{}}/products/{{}}/consumption/invoice-estimate"
VIRTUAL_BATTERY_HISTORY_URL = f"{BASE_API_URL}houses/{{}}/products/{{}}/virtual-battery/history"

# Frecuencia de actualización
UPDATE_INTERVAL = timedelta(minutes=120)

# Cabeceras comunes (mínimas y estables)
COMMON_HEADERS = {
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    ),
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
    "Market": "ES",
    "x-origin": "WEB",
}

# Cabeceras de login
LOGIN_HEADERS = {
    **COMMON_HEADERS,
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://areacliente.repsol.es",
    "Referer": "https://areacliente.repsol.es/",
}

# Cabeceras para peticiones autenticadas (las credenciales UID/firmas se añaden en runtime)
CONTRACTS_HEADERS = {
    **COMMON_HEADERS,
    "Origin": "https://areacliente.repsol.es",
    "Referer": "https://areacliente.repsol.es/mis-hogares",
}

# Cookies “bootstrap” (la API suele aceptarlas; mantenlas como estaban si te funcionan)
COOKIES_CONST = {
    "gmid": "gmid.ver4.AtLtj-S6Bg.5nGvNQiXUMMFW5Z7o3A2mIP4kjnCrm-CtwscvU8NC2FhNb6dxX09HfdUzL3pI26o.SHj7Fh8B8OK5xpZyFyZUX6mtQeRTaEhz_FtBwVbr_-5l6b8u6iBOOR6aoh7B-2kdAVrB3ro8ysuq1sEGjriOfQ.sc3",
    "ucid": "fXMDPs47yZukqcRaCm6LKQ",
    "hasGmid": "ver4",
    "gig_bootstrap_3_jm2BKK8jIBHi9nXHP8OsQ-HNgJKWxgd1o6kbNqsWvhUy0hhD1eeCpHC-qCrrWe8D": "login_ver4",
}

# Payload base de login (el usuario/contraseña se añaden en runtime)
LOGIN_DATA = {
    "targetEnv": "jssdk",
    "includeUserInfo": "true",
    "include": "profile,data,preferences,",
    "lang": "es",
    "sdk": "js_latest",
    "APIKey": "3_jm2BKK8jIBHi9nXHP8OsQ-HNgJKWxgd1o6kbNqsWvhUy0hhD1eeCpHC-qCrrWe8D",
    "format": "json",
}
