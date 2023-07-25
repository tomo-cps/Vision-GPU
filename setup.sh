#!/bin/bash
# 引数には以下のようにユーザ名と conda 環境の名前を指定してください
# bash setup.sh tomo anaconda3
source ~/"$2"/etc/profile.d/conda.sh
y | conda create -n vig python==3.9
conda activate vig
cd backend/
pip install -r requirements.txt

cd /etc/systemd/system/
sudo git clone https://github.com/tomo-cps/Visual-GPU.git
cat << EOF | sudo tee -a /etc/systemd/system/vig-app.service
[Unit]
Description=FastAPI Application
After=network.target

[Service]
User=root
WorkingDirectory=/etc/systemd/system/Visual-GPU/backend/
ExecStart=/home/"$1"/"$2"/envs/vig/bin/uvicorn fast:app --host 0.0.0.0 --port 8000
Restart=always
StandardOutput=file:/var/log/vig-app.log
StandardError=file:/var/log/vig-app.log

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl start vig-app
sudo systemctl status vig-app


