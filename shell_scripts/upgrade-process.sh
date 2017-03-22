# sudo setcap 'cap_net_raw,cap_net_admin,cap_net_bind_service+eip' /usr/bin/nmap
# sudo setcap 'cap_net_bind_service,cap_net_raw+eip' /srv/homeassistant/homeassistant_venv/bin/python3
source /srv/homeassistant/homeassistant_venv/bin/activate
pip3 install --upgrade homeassistant
# sudo systemctl restart home-assistant
