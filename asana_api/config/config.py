from dotenv import load_dotenv
from utils.crypto import generate_key, encrypt_token, decrypt_token
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
# TOKEN = '2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24'

key = generate_key()
encrypted_token = encrypt_token(TOKEN, key)
decrypted_token = decrypt_token(encrypted_token, key)

# Headers
COMMON_HEADERS = {
    'authorization': f'Bearer {decrypted_token}',
    'accept': 'application/json'
}

CONTENT_HEADERS = {
    **COMMON_HEADERS,
    'content-Type': 'application/json'
}

# Asana
ASANA_API_URL = 'https://app.asana.com/api/1.0'
WORKSPACE_ID = '1206761420534796'
TEST_PROJECT_NAME = "OM - New Project"

CREATE_PROJECT_URL = f'{ASANA_API_URL}/workspaces/{WORKSPACE_ID}/projects'
PROJECT_URL = lambda project_id: f'{ASANA_API_URL}/projects/{project_id}'
