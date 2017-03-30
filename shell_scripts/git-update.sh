#! /bin/bash

# If it config validation fails, stop script
echo "Validating configuration..."
source /srv/homeassistant/homeassistant_venv/bin/activate

if hass --script check_config; then

cd /home/homeassistant/.homeassistant
git add .
git status
echo -n "Enter the Description for the Change: " [Minor Update]
read CHANGE_MSG
git commit -m "${CHANGE_MSG}"
git push origin master

else

echo "Script validation failed"
exit 1

fi

exit
