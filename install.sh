#!/bin/bash

read -sp "Do you want to install hackzero.inpututils? [y/n]: " iutils

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

iutils_path="$SCRIPT_DIR/hackzero/inpututils"

if ["${iutils,}" = "y"]; then
    touch /etc/systemd/system/hackzero-inpututils.service
    {
        echo '[Unit]'
        echo 'Description=GPIO Dpad to keyboard utility'
        echo 'After=multi-user.target'
        echo ''
        echo '[Service]'
        echo 'Type=simple'
        echo 'WorkingDirectory=$iutils_path'
        echo 'ExecStart=$iutils_path/'
        echo 'KillSignal=SIGINT'
        echo 'Restart=on-failure'
        echo ''
        echo '[Install]'
        echo 'WantedBy=multi-user.target'
    } >| /etc/systemd/system/hackzero-inpututils.service
    sudo chmod 644 /etc/systemd/system/hackzero-inpututils.service
    sudo chown root:root /etc/systemd/system/hackzero-inpututils.service
    sudo systemctl daemon-reload
    sudo systemctl enable hackzero-inpututils
    sudo systemctl start hackzero-inpututils
fi

echo 'Installed hackzero.inpututils'

sudo chmod +X $SCRIPT_DIR/updater.sh

pip install keyboard PyQt5