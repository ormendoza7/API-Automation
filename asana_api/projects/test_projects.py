import logging
import pytest
import requests
from config.config import ASANA_API_URL, CONTENT_HEADERS, COMMON_HEADERS, WORKSPACE_ID, TEST_PROJECT_NAME
from utils.logger import get_logger


LOGGER = get_logger(__name__, logging.DEBUG)


def test_create_project(project_created):
    project_id = project_created['gid']

    assert project_id is not None, "Project ID should not be None."
    LOGGER.debug("Project id: %s", project_id)
    LOGGER.debug("Response created: %s", project_created)


def test_read_project(project_created):
    project_id = project_created['gid']
    url = f'{ASANA_API_URL}/projects/{project_id}'

    response = requests.get(url, headers=COMMON_HEADERS)

    assert response.status_code == 200
    assert response.json()['data']['gid'] == project_id
    LOGGER.debug("Project id: %s", project_id)
    LOGGER.debug("Project created: %s", project_created)

def test_update_project(project_created):
    project_id = project_created['gid']
    url = f'{ASANA_API_URL}/projects/{project_id}'
    updated_name = "OM - Updated Project"
    data = {'data': {'name': updated_name}}

    response = requests.put(url, headers=CONTENT_HEADERS, json=data)

    assert response.status_code == 200
    assert updated_name in response.json()['data']['name']
    LOGGER.debug("Project id: %s", project_id)
    LOGGER.debug("Project updated: %s", response.json()['data'])

def test_delete_project():
    # Create Project to Delete
    url = f'{ASANA_API_URL}/workspaces/{WORKSPACE_ID}/projects'
    data = {'data': {'name': TEST_PROJECT_NAME}}

    response = requests.post(url, headers=CONTENT_HEADERS, json=data)
    assert response.status_code == 201

    # Delete Project
    project_id = response.json()['data']['gid']
    url = f'{ASANA_API_URL}/projects/{project_id}'

    response = requests.delete(url, headers=COMMON_HEADERS)

    assert response.status_code == 200

    # Check
    response = requests.get(url, headers=COMMON_HEADERS)
    assert response.status_code == 404
    LOGGER.debug("Project id: %s", project_id)