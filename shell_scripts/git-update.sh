#! /bin/bash

# Run script validation
source /srv/homeassistant/homeassistant_venv/bin/activate
hass --script check_config

# If it fails, stop script
if [ $? != 0 ]; then
   echo "Error, config validation failed"
   exit
fi

cd /home/homeassistant/.homeassistant
git add .
git status
echo -n "Enter the Description for the Change: " [Minor Update]
read CHANGE_MSG
git commit -m "${CHANGE_MSG}"
git push origin master

exit
