#!/bin/bash

echo "Installing Flirc remote dependencies"
sudo apt-get update
sudo apt-get -y install brutefir
echo "Installing brutefir plugin"

echo "snd_aloop" > /etc/modules

#requred to end the plugin install
echo "plugininstallend"
