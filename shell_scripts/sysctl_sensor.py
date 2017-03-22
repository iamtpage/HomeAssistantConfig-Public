import requests
import json
import subprocess
import time

# Sysctl sensor

# URL for homeassistant instance
hass_url = "http://thor.vik/api/states/sysctl."

# Headers for homeassistant instance
hass_headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'x-ha-access': 'hunter2'}

# Services I want to track
services = ["bluetooth.service","cron.service","dasher.service","dhcpcd.service","dnsmasq.service","habridge.service","nginx.service","ntp.service","php5-fpm.service","ssh.service","supervisor.service"]

for service in services:

  # Get status information from systemctl
  service_info = subprocess.check_output("systemctl is-active " + service + "; exit 0", stderr=subprocess.STDOUT, shell=True).decode('utf-8').replace("\n","")

  # Generate payload for HASS
  hass_payload = {
        "state": service_info,
        "attributes": {
             "friendly_name": service.replace("."," ")
        }
  }

  # Formate sensor name to be <service>_service instead of <service>.service
  hass_sensor = service.replace(".","_")
  hass_sensor = hass_sensor.replace("-","_")

  # POST data to HASS
  hass_request = requests.post(hass_url + hass_sensor, headers=hass_headers, data=json.dumps(hass_payload))

  # Sleep to not block CPU
  time.sleep(5)
