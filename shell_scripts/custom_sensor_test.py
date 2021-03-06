import requests
import json

# Custom sensor python script

# Replace <HA_URL> with your HA's url (Example: 192.168.x.x or my-homeassistant.duckdns.org)
hass_url = "http://thor.vik"

# Replace <HA_PORT> with your installation's port number (8123 by default, or 80 if using dynamic dns)
hass_port = "80"

# Replace <HA_PASSWORD> with your api_password you defined in configuration.yaml
hass_password = "hunter2"

# Replace <HA_SENSOR_NAME> with what you want your sensor's name to be
hass_sensor_name = "sensor.test"

# Replace <HA_SENSOR_FRIENDLY_NAME> with what you want your sensor's friendly_name attribute to be
hass_sensor_friendly_name = "test sensor"

# Replace <HA_SENSOR_STATE> with the state you want your sensor to be
hass_sensor_state = "online"

# Example of an attribute list if necessary
hass_sensor_attributes = {"attribute1": "value1", "friendly_name": hass_sensor_friendly_name}

# Build the URL based on variables defined above
hass_endpoint = hass_url + ":" + hass_port + "/api/states/" + hass_sensor_name

# Define headers for HASS
hass_headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'x-ha-access': hass_password}

# Generate payload for HASS
hass_payload = {
      "state": hass_sensor_state,
      "attributes": hass_sensor_attributes
}

# POST data to HASS
hass_request = requests.post(hass_endpoint, headers=hass_headers, data=json.dumps(hass_payload))
print(hass_request.text)
