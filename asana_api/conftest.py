import pytest
import requests
import logging
from config.config import CONTENT_HEADERS, COMMON_HEADERS, TEST_PROJECT_NAME, CREATE_PROJECT_URL, PROJECT_URL
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.INFO)


@pytest.fixture()
#@pytest.fixture(scope="module")
def project_created():
    # Create Project
    LOGGER.info("Starting project creation fixture.")

    data = {'data': {'name': TEST_PROJECT_NAME}}

    response = requests.post(CREATE_PROJECT_URL, headers=CONTENT_HEADERS, json=data)
    assert response.status_code == 201

    project = response.json()['data']
    assert TEST_PROJECT_NAME == project['name']

    LOGGER.info(f"Project created with ID: {project['gid']} and name: {TEST_PROJECT_NAME}")
    yield project

    # Delete Project
    LOGGER.info(f"Cleaning up project with ID: {project['gid']}.")
    project_id = project['gid']
    response = requests.delete(PROJECT_URL(project_id), headers=COMMON_HEADERS)
    assert response.status_code == 200
    LOGGER.info(f"Project with ID: {project['gid']} deleted successfully.")