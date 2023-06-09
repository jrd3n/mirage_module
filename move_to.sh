#!/bin/bash

sudo cp ./ble_BULB.py /root/.mirage/modules/ble_BULB.py
sudo cp ./ble_bulb_scene.py /root/.mirage/scenarios/ble_bulb_scene.py

sudo cp ./ble_JORDON.py /root/.mirage/modules/ble_JORDON.py
sudo cp ./ble_trial_scene.py /root/.mirage/scenarios/ble_trial_scene.py

echo "Moved!"

# sudo cat /root/.mirage/modules/ble_BULB.py