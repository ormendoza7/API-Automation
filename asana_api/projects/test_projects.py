import requests
import logging
from config.config import CONTENT_HEADERS, COMMON_HEADERS, TEST_PROJECT_NAME, CREATE_PROJECT_URL, PROJECT_URL
from utils.logger import get_logger

LOGGER = get_logger(__name__, logging.INFO)


class TestProject:
    def test_create_project(self, project_created):
        project_id = project_created['gid']

        assert project_id is not None, "Project ID should not be None."
        LOGGER.info(f"Project created successfully with ID: {project_created['gid']}.")

    def test_read_project(self, project_created):
        project_id = project_created['gid']

        response = requests.get(PROJECT_URL(project_id), headers=COMMON_HEADERS)

        assert response.status_code == 200
        assert response.json()['data']['gid'] == project_id
        LOGGER.info(f"Project read successfully with ID: {project_created['gid']}.")

    def test_update_project(self, project_created):
        project_id = project_created['gid']
        updated_name = "OM - Updated Project"
        data = {'data': {'name': updated_name}}

        response = requests.put(PROJECT_URL(project_id), headers=CONTENT_HEADERS, json=data)

        assert response.status_code == 200
        assert updated_name in response.json()['data']['name']
        LOGGER.info(f"Project updated successfully with ID: {project_created['gid']} to name: {updated_name}.")

    def test_delete_project(self):
        # Create Project to Delete
        data = {'data': {'name': TEST_PROJECT_NAME}}

        response = requests.post(CREATE_PROJECT_URL, headers=CONTENT_HEADERS, json=data)
        assert response.status_code == 201

        # Delete Project
        project_id = response.json()['data']['gid']

        response = requests.delete(PROJECT_URL(project_id), headers=COMMON_HEADERS)

        assert response.status_code == 200

        # Check
        response = requests.get(PROJECT_URL(project_id), headers=COMMON_HEADERS)
        assert response.status_code == 404
        LOGGER.info(f"Project deleted successfully with ID: {project_id}.")