from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
import requests

app = Flask(__name__)
swagger = Swagger(app)

#GRAFANA_API_URL = "http://localhost:3000/api/search"
#GRAFANA_API_TOKEN = "glsa_icqAfZecHkWTpahAtQ7XuKaTaFJKJhAs_c3b94302"

@app.route('/api/getDashboards', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'grafana_base_url',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Grafana API URL'
        },
        {
            'name': 'grafana_token',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Grafana API Token'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of dashboards',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'isStarred': {'type': 'boolean'},
                        'slug': {'type': 'string'},
                        'sortMeta': {'type': 'integer'},
                        'tags': {
                            'type': 'array',
                            'items': {'type': 'string'}
                        },
                        'title': {'type': 'string'},
                        'type': {'type': 'string'},
                        'uid': {'type': 'string'},
                        'uri': {'type': 'string'},
                        'url': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def get_dashboards():
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400

    grafana_url = grafana_base_url + "/api/search"

    headers = {
        "Authorization": f"Bearer {grafana_token}"
    }
    response = requests.get(grafana_url, headers=headers)

    if response.status_code == 200:
        dashboards = response.json()
        return jsonify(dashboards)
    else:
        return jsonify({"error": "Unable to fetch dashboards"}), response.status_code


@app.route('/api/getDashboard/<string:id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'grafana_base_url',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Grafana API URL'
        },
        {
            'name': 'grafana_token',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Grafana API Token'
        },
        {
            'name': 'id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'Id of dashboard to fetch'
        }
    ],
    'responses': {
        200: {
            'description': 'Dashboard details',
        }
    }
})
def get_dashboard_by_id(id):
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400

    grafana_url = grafana_base_url + f"/api/dashboards/uid/{id}"

    headers = {
        "Authorization": f"Bearer {grafana_token}"
    }
    response = requests.get(grafana_url, headers=headers)

    if response.status_code == 200:
        dashboard = response.json()
        return jsonify(dashboard)
    else:
        return jsonify({"error": f"There is no dashboard with this id {id}"}), response.status_code

@app.route('/api/getDatasources', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'grafana_base_url',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Grafana API URL'
        },
        {
            'name': 'grafana_token',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Grafana API Token'
        }
    ],
    'responses': {
        200: {
            'description': 'A list of datasources',
        }
    }
})
def get_datasources():
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400

    grafana_url = grafana_base_url + "/api/datasources"

    headers = {
        "Authorization": f"Bearer {grafana_token}"
    }
    response = requests.get(grafana_url, headers=headers)

    if response.status_code == 200:
        datasources = response.json()
        return jsonify(datasources)
    else:
        return jsonify({"error": "Unable to fetch datasources"}), response.status_code

@app.route('/api/getDatasource/<string:id>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'grafana_base_url',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Grafana API URL'
        },
        {
            'name': 'grafana_token',
            'in': 'query',
            'type': 'string',
            'required': True,
            'description': 'Grafana API Token'
        },
        {
            'name': 'id',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'Id of datasource to fetch'
        }
    ],
    'responses': {
        200: {
            'description': 'Datasource details',
        }
    }
})
def get_datasource_by_id(id):
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400

    grafana_url = grafana_base_url + f"/api/datasources/uid/{id}"

    headers = {
        "Authorization": f"Bearer {grafana_token}"
    }
    response = requests.get(grafana_url, headers=headers)

    if response.status_code == 200:
        datasource = response.json()
        return jsonify(datasource)
    else:
        return jsonify({"error": f"There is no datasource with this id {id}"}), response.status_code

@app.route('/api/migrate/<string:from_ds>/<string:to_ds>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'from_ds',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'Type of from datasource'
        },
        {
            'name': 'to_ds',
            'in': 'path',
            'type': 'string',
            'required': True,
            'description': 'Type of to datasource'
        }
    ],
    'responses': {
        200: {
            'description': 'Migration result',
            'schema': {
                'type': 'object',
                'properties': {
                    'from': {'type': 'string'},
                    'to': {'type': 'string'},
                    'status': {'type': 'string'}
                }
            }
        }
    }
})
def migrate_datasource(from_ds, to_ds):
    # Replace with actual Grafana API call and logic
    result = {'from': from_ds, 'to': to_ds, 'status': 'success'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=8090)
