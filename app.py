from flask import Flask, request, jsonify
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

def get_grafana_headers(grafana_token): # Returns headers for Grafana API requests
    return {
        "Authorization": f"Bearer {grafana_token}",
        "Content-Type": "application/json"
    }

@app.route('/api/getDashboards', methods=['GET'])
def get_dashboards():   # Returns all dashboards
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    # Send error if the required parameters are not provided
    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400

    # Construct the URL and headers for the request
    grafana_url = grafana_base_url + "/api/search"
    headers = get_grafana_headers(grafana_token)

    # Send a request to Grafana API
    response = requests.get(grafana_url, headers=headers)

    # Return the dashboards if the request is successful
    if response.status_code == 200:
        dashboards = response.json()
        return jsonify(dashboards)
    else:
        return jsonify({"error": "Unable to fetch dashboards"}), response.status_code

@app.route('/api/getDashboard/<string:id>', methods=['GET'])
def get_dashboard_by_id(id):    # Returns a dashboard by its UID
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    # Send error if the required parameters are not provided
    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400

    # Construct the URL and headers for the request
    grafana_url = grafana_base_url + f"/api/dashboards/uid/{id}"
    headers = get_grafana_headers(grafana_token)

    # Send a request to Grafana API
    response = requests.get(grafana_url, headers=headers)

    # Return the dashboard if the request is successful
    if response.status_code == 200:
        dashboard = response.json()
        return jsonify(dashboard)
    else:
        return jsonify({"error": f"There is no dashboard with this id {id}"}), response.status_code

@app.route('/api/getDatasources', methods=['GET'])
def get_datasources():  # Returns all datasources
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    # Send error if the required parameters are not provided
    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400

    # Construct the URL and headers for the request
    grafana_url = grafana_base_url + "/api/datasources"
    headers = get_grafana_headers(grafana_token)
    
    # Send a request to Grafana API
    response = requests.get(grafana_url, headers=headers)

    # Return the datasources if the request is successful
    if response.status_code == 200:
        datasources = response.json()
        return jsonify(datasources)
    else:
        return jsonify({"error": "Unable to fetch datasources"}), response.status_code

@app.route('/api/getDatasource/<string:id>', methods=['GET'])
def get_datasource_by_id(id): # Returns a datasource by its UID
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    # Send error if the required parameters are not provided
    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400

    # Construct the URL and headers for the request
    grafana_url = grafana_base_url + f"/api/datasources/uid/{id}"
    headers = get_grafana_headers(grafana_token)

    # Send a request to Grafana API
    response = requests.get(grafana_url, headers=headers)

    # Return the datasource if the request is successful
    if response.status_code == 200:
        datasource = response.json()
        return jsonify(datasource)
    else:
        return jsonify({"error": f"There is no datasource with this id {id}"}), response.status_code
    
@app.route('/api/migrate/<string:from_type>/<string:to_type>', methods=['GET'])
def migrate_datasource(from_type, to_type): # Migrates all datasources from one type to another
    grafana_base_url = request.args.get('grafana_base_url')
    grafana_token = request.args.get('grafana_token')

    # Send error if the required parameters are not provided
    if not grafana_base_url or not grafana_token:
        return jsonify({"error": "Grafana URL and token are required"}), 400
    

    if from_type == "ELASTIC":
        from_type = "elasticsearch"
    else: return jsonify({"error": "Invalid from datasource type"}), 400

    if to_type == "OPENSEARCH":
        to_type = "grafana-opensearch-datasource"
    else: return jsonify({"error": "Invalid to datasource type"}), 400


    # Get all dashboards
    dashboards_response = get_dashboards()
    dashboards = dashboards_response.get_json()
    headers = get_grafana_headers(grafana_token)

    # Get all datasources to use later
    datasources_response = get_datasources()
    datasources = datasources_response.get_json()

    # Loop through each dashboard
    for dashboard in dashboards:
        dashboard_details_response = get_dashboard_by_id(dashboard['uid'])
        if dashboard_details_response.status_code != 200:
            continue

        dashboard_details = dashboard_details_response.get_json()
        dashboard_json = dashboard_details['dashboard']
        updated = False

        # Update each panel's datasource
        for panel in dashboard_json.get('panels', []):
            if panel.get('datasource', {}).get('type') == from_type:
                datasource_uid = panel['datasource']['uid']
                datasource_response = get_datasource_by_id(datasource_uid)
                if datasource_response.status_code == 200:
                    datasource_details = datasource_response.get_json()
                    database_name = datasource_details['jsonData']['index']

                    matched_ds = None
                    for ds in datasources:
                        if ds['jsonData'].get('database') == database_name and ds['type'] == to_type:
                            matched_ds = ds
                            break

                    if matched_ds:
                        panel['datasource']['type'] = to_type
                        panel['datasource']['uid'] = matched_ds['uid']
                        updated = True

                        # Change the type of the datasource in the targets of the panel
                        for target in panel.get('targets', []):
                            target['datasource']['type'] = to_type
                            target['datasource']['uid'] = matched_ds['uid']

        if updated:
            # Update the dashboard with new datasource
            update_response = requests.post(
                f"{grafana_base_url}/api/dashboards/db",
                headers=headers,
                json={"dashboard": dashboard_json, "overwrite": True}
            )
            if update_response.status_code != 200:
                return jsonify({"error": "Failed to update dashboard"}), update_response.status_code

    return jsonify({"message": "Datasource migration successful"}), 200


if __name__ == '__main__':
    app.run(port=8090)
