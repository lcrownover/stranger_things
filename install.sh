#!/bin/bash

#Files
mkdir /opt/stranger_things
cp -rp app/web/ /opt/stranger_things

#Deps
pip3 install -r /opt/stranger_things/web/requirements.txt

#Service
cp -rp app/stranger_things_web.service /lib/systemd/system/
systemctl enable stranger_things_web.service
systemctl start stranger_things_web.service
