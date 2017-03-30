#! /bin/bash

# Stops HA, clears the error log, validates the config, and starts HA again
echo "Stopping HA..."
sudo systemctl stop home-assistant.service

echo "Clearing home-assistant.log"
rm /home/homeassistant/.homeassistant/home-assistant.log
touch /home/homeassistant/.homeassistant/home-assistant.log

echo "Validating configuration..."
source /srv/homeassistant/homeassistant_venv/bin/activate

if hass --script check_config; then
    echo "Validation of config passed"
    echo "Starting HA..."
    sudo systemctl start home-assistant.service
else
    echo "Validation of config failed"
    echo "Exiting..."
fi
