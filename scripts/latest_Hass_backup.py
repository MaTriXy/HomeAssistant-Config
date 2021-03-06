#!/bin/bash

#this script will check the last time backup was made
cd /config/backup/hass/ | ls -lat --time-style=+"%d-%m %H:%M" | head -n 2 | grep -o '[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]'

#Old way - to get MM-DD result
#find /config/backup/hass/ -type f -exec stat \{} --printf="%y\n" \; | sort -n -r | head -n 1 | grep -o '[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]'
