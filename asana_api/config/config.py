# Asana
ASANA_API_URL = 'https://app.asana.com/api/1.0'
WORKSPACE_ID = '1206761420534796'
TEST_PROJECT_NAME = "OM - New Project"

# Headers
BEARER_TOKEN = 'Bearer 2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24'

COMMON_HEADERS = {
    'authorization': BEARER_TOKEN,
    'accept': 'application/json'
}

CONTENT_HEADERS = {
    **COMMON_HEADERS,
    'content-Type': 'application/json'
}
