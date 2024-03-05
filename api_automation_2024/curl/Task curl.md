**Create CURL request using an API:**

Basic CRUD(Read, Create, Update, Delete):

Negative cases at least 4:

## **Create Project in a work space**

```bash
curl --request POST 'https://app.asana.com/api/1.0/workspaces/1206761420534796/projects' \
	--header 'accept: application/json' \
	--header 'authorization: Bearer 2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24' \
	--header 'content-type: application/json' \
	--header 'Cookie: logged_out_uuid=01536ea49a37082d7dd72f8d501aa54c; xsrf_token=50da3377a3c41a91c015ca3767f46064%3A1709605190128' \
	--data '{
		"data": {
			"name": "OM - New project"
		}
	}'
```

**Response:**
```
{"data":{"gid":"1206761664935906","resource_type":"project","created_at":"2024-03-05T03:19:13.698Z","modified_at":"2024-03-05T03:19:13.698Z","owner":{"gid":"1206761420534786","resource_type":"user","name":"Orlando Mendoza"},"due_date":null,"due_on":null,"current_status_update":null,"current_status":null,"public":true,"name":"OM - New project","notes":"","archived":false,"workspace":{"gid":"1206761420534796","resource_type":"workspace","name":"Mi espacio de trabajo"},"team":{"gid":"1206761420534798","resource_type":"team","name":"Mi espacio de trabajo"},"permalink_url":"https://app.asana.com/0/1206761664935906/1206761664935906","default_view":"list","default_access_level":"editor","minimum_access_level_for_customization":"editor","minimum_access_level_for_sharing":"editor","start_on":null,"completed":false,"completed_at":null,"completed_by":null,"members":[{"gid":"1206761420534786","resource_type":"user","name":"Orlando Mendoza"}],"followers":[{"gid":"1206761420534786","resource_type":"user","name":"Orlando Mendoza"}],"custom_fields":[],"custom_field_settings":[],"color":null,"icon":"list"}}
```

## **Get project by Id**
```bash
curl --request GET \
     --url https://app.asana.com/api/1.0/projects/1206761664935906 \
     --header 'accept: application/json' \
     --header 'authorization: Bearer 2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24'
```
**Response:**
```
{"data":{"gid":"1206761664935906","archived":false,"color":null,"completed":false,"completed_at":null,"created_at":"2024-03-05T03:19:13.698Z","current_status":null,"current_status_update":null,"custom_fields":[],"custom_field_settings":[],"default_access_level":"editor","default_view":"list","due_on":null,"due_date":null,"followers":[{"gid":"1206761420534786","name":"Orlando Mendoza","resource_type":"user"}],"members":[{"gid":"1206761420534786","name":"Orlando Mendoza","resource_type":"user"}],"minimum_access_level_for_customization":"editor","minimum_access_level_for_sharing":"editor","modified_at":"2024-03-05T03:19:14.762Z","name":"OM - New project","notes":"","owner":{"gid":"1206761420534786","name":"Orlando Mendoza","resource_type":"user"},"permalink_url":"https://app.asana.com/0/1206761664935906/1206761664935906","public":true,"resource_type":"project","start_on":null,"team":{"gid":"1206761420534798","name":"Mi espacio de trabajo","resource_type":"team"},"workspace":{"gid":"1206761420534796","name":"Mi espacio de trabajo","resource_type":"workspace"}}}
```

## **Update a project name**
```bash
curl --request PUT \
     --url https://app.asana.com/api/1.0/projects/1206761664935906\
     --header 'accept: application/json' \
     --header 'authorization: Bearer 2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24' \
     --header 'content-type: application/json' \
	 --data '{
		"data": {
			"name": "OM - New project updated"
		}
	}'
```
**Response:**
```
{"data":{"gid":"1206761664935906","resource_type":"project","created_at":"2024-03-05T03:19:13.698Z","modified_at":"2024-03-05T03:19:14.762Z","owner":{"gid":"1206761420534786","resource_type":"user","name":"Orlando Mendoza"},"due_date":null,"due_on":null,"current_status_update":null,"current_status":null,"public":true,"name":"OM - New project updated","notes":"","archived":false,"workspace":{"gid":"1206761420534796","resource_type":"workspace","name":"Mi espacio de trabajo"},"team":{"gid":"1206761420534798","resource_type":"team","name":"Mi espacio de trabajo"},"permalink_url":"https://app.asana.com/0/1206761664935906/1206761664935906","default_view":"list","default_access_level":"editor","minimum_access_level_for_customization":"editor","minimum_access_level_for_sharing":"editor","start_on":null,"completed":false,"completed_at":null,"completed_by":null,"members":[{"gid":"1206761420534786","resource_type":"user","name":"Orlando Mendoza"}],"custom_field_settings":[],"custom_fields":[],"color":null,"followers":[{"gid":"1206761420534786","resource_type":"user","name":"Orlando Mendoza"}],"icon":"list"}}
```

## **Delete project by id**
```bash
curl --request DELETE \
     --url https://app.asana.com/api/1.0/projects/1206761664935906 \
     --header 'accept: application/json' \
     --header 'authorization: Bearer 2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24'
```
**Response:**
```
{"data":{}}
```

## **Negative testing**

## **Create a project with an invalid body:**
```bash
curl --request POST 'https://app.asana.com/api/1.0/workspaces/1206761420534796/projects' \
	--header 'accept: application/json' \
	--header 'authorization: Bearer 2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24' \
	--header 'content-type: application/json' \
	--header 'Cookie: logged_out_uuid=01536ea49a37082d7dd72f8d501aa54c; xsrf_token=50da3377a3c41a91c015ca3767f46064%3A1709605190128' \
	--data '{
			"name": "OM - New project"
			}'
```
**Response:**
```
{"errors":[{"message":"Unrecognized request field `name`. The only allowed keys at the top level are: data, options. Is it possible you did not wrap object properties in a `data` object?","help":"For more information on API status codes and how to handle them, read the docs on errors: https://developers.asana.com/docs/errors"}]}
```
## **Get a project with a non-existent id**
```bash
curl --request GET \
     --url https://app.asana.com/api/1.0/projects/1206761664935512 \
     --header 'accept: application/json' \
     --header 'authorization: Bearer 2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24'
```
**Response:**
```
{"errors":[{"message":"project: Not a recognized ID: 1206761664935512","help":"For more information on API status codes and how to handle them, read the docs on errors: https://developers.asana.com/docs/errors"}]}
```
## **Update a project with an invalid method**
```bash
curl --request POST \
     --url https://app.asana.com/api/1.0/projects/1206761664935906\
     --header 'accept: application/json' \
     --header 'authorization: Bearer 2/1206761420534786/1206761422460081:c33b2c837465d541459309eb57872d24' \
     --header 'content-type: application/json' \
	 --data '{
		"data": {
			"name": "OM - New project updated"
		}
	}'
```
## **Delete a project with an invalid token**
```bash
curl --request DELETE \
     --url https://app.asana.com/api/1.0/projects/1206761664935906 \
     --header 'accept: application/json' \
     --header 'authorization: Bearer 2/1206761420534786/1206761422460081:c1234567890'
```
**Response:**
```
{"errors":[{"message":"Not Authorized","help":"For more information on API status codes and how to handle them, read the docs on errors: https://developers.asana.com/docs/errors"}]}
```