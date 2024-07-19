from flask import Flask, request, jsonify, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
import requests

app = Flask(__name__)

# Swagger UI setup
SWAGGER_URL = '/swagger-ui.html'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Grafana API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/api/getDashboards', methods=['GET'])
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

if __name__ == '__main__':
    app.run(port=8090)
