#!/bin/sh 
#
# 
#  ________    ______  _______    
# |_   __  | .' ___  ||_   __ \   𝘍𝘦𝘳𝘯𝘢𝘯𝘥𝘰 𝘎. 𝘗𝘳𝘪𝘦𝘵𝘰
#   | |_ \_|/ .'   \_|  | |__) |  𝘩𝘵𝘵𝘱𝘴://𝘨𝘪𝘵𝘩𝘶𝘣.𝘤𝘰𝘮/𝘧𝘦𝘳𝘯𝘢𝘯𝘥𝘰𝘨𝘱𝘳𝘪𝘦𝘵𝘰/
#   |  _|   | |   ____  |  ___/   𝘩𝘵𝘵𝘱𝘴://𝘵𝘸𝘪𝘵𝘵𝘦𝘳.𝘤𝘰𝘮/𝘧𝘦𝘳𝘯𝘢𝘯𝘥𝘰𝘨𝘱𝘳𝘪𝘦𝘵𝘰
#  _| |_    \ `.___]  |_| |_      
# |_____|    `._____.'|_____| 
#
#      


#python3-gi = python-gobject
# Xmonad only for a few config if you want!
# sudo apt-get install xmonad libghc-xmonad-contrib-dev libghc-xmonad-dev 
sudo apt-get install lxappearance fish suckless-tools python3 python3-pip libpangocairo-1.0-0 alsa-utils pavucontrol pcmanfm suckless-tools python3-gi libx11-dev libxft-dev libxinerama-dev -y
pip3 install xcffib dbus-python autokey dbus-next
pip3 install --no-cache-dir cairocffi

#if you have a problem you can install python-dbus-devlibdbus-1-dev libdbus-glib-1-dev
git clone git://github.com/qtile/qtile.git
cd qtile/
pip3 install .
sudo reboot
vim .xinitrc 
qtile start
sudo reboot

#at this moment you can modify  qtile and st with your prefered configs.
startx

#if you have problem with lib remove ~/.cache/pip/
pip uninstall cairocffi
pip install --no-deps --ignore-installed cairocffi
cd qtile/
pip3 install .
sudo reboot
