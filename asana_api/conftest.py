import pytest
import requests
import logging
from config.config import ASANA_API_URL, CONTENT_HEADERS, COMMON_HEADERS, WORKSPACE_ID, TEST_PROJECT_NAME
from utils.logger import get_logger


LOGGER = get_logger(__name__, logging.DEBUG)
@pytest.fixture()
def project_created():
    # Create Project
    LOGGER.debug("Create project fixture")

    url = f'{ASANA_API_URL}/workspaces/{WORKSPACE_ID}/projects'
    data = {'data': {'name': TEST_PROJECT_NAME}}

    response = requests.post(url, headers=CONTENT_HEADERS, json=data)
    project = response.json()['data']
    assert response.status_code == 201
    assert TEST_PROJECT_NAME == project['name']

    yield project

    # Delete Project
    LOGGER.info("Cleanup project...")
    project_id = project['gid']
    url = f'{ASANA_API_URL}/projects/{project_id}'
    response = requests.delete(url, headers=COMMON_HEADERS)
    assert response.status_code == 200
    LOGGER.info("Project Id: %s deleted", project_id)