import requests
import json
import time

# Dataplicity sensor

# URLs for dataplicity api and homeassistant instance
url = "https://apps.dataplicity.com"
hass_url = "http://thor.vik/api/states/sensor.dataplicity"

# Headers for dataplicity api and homeassistant instance
headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Token aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'}
hass_headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'x-ha-access': 'hunter'}

# Format payload to get token from authentication request
#payload = {
#    "email": "asdasd@gmail.com",
#    "password": "hunter2"
#}

# Set flag so we only authenticate once
#flag = False

counter = 0

# Infinite loops!
while counter < 5:

  # Get devices in account
  request = requests.get(url + "/devices/", headers=headers)

  # If we DON'T get a server error message
  if(request.status_code != 502):

    # Parse the JSON and extract the data we want
    devices_json = request.json()

    dataplicity_url = "https://" + devices_json[0]['wormhole_slug'] + ".dataplicity.io"

    dataplicity_version = str(devices_json[0]["agent_version"])

    dataplicity_name = str(devices_json[0]["name"])

    dataplicity_status = str(devices_json[0]["online"])

    dataplicity_type = str(devices_json[0]["machine_type_short_display"])

    # Ports URL means in the future we can dynamically forward ports through dataplicity
    #ports_url = str(devices_json[0]["ports_url"])

    # This formats the sensor state in HASS
    if(str(devices_json[0]["online"]) == "True"):
      dataplicity_state = "on"

    else:
      dataplicity_state = "off"

    # Generate payload for HASS
    hass_payload = {
          "state": dataplicity_state,
          "attributes": {
                "wormhole_url": "" + dataplicity_url + "",
                "version": "" + dataplicity_version + "",
                "name": "" + dataplicity_name + "",
                "type": "" + dataplicity_type + ""
          }
    }

    # POST dataplicity data to HASS
    hass_request = requests.post(hass_url, headers=hass_headers, data=json.dumps(hass_payload))
    counter += 1

  else:
    counter += 1
    continue

  # Sleep so we don't use too much CPU
  time.sleep(5)
