# Visual-GPU
## Frontend

```
npm install 
```

```
npm run serve
```

## Backend
### 仮想環境の構築

```
y | conda create -n vig python==3.9
conda activate vig
git clone https://github.com/tomo-cps/Visual-GPU.git
cd Visual-GPU/backend 
pip install -r requrements.txt
cd ../../
rm -rf Visual-GPU/
```

### systemd を用いて常に FastAPI を実行させておく
```
cd /etc/systemd/system/
sudo git clone https://github.com/tomo-cps/Visual-GPU.git
sudo emacs /etc/systemd/system/vig-app.service
```
↓ vig-app.service に追記する
```
[Unit]
Description=FastAPI Application
After=network.target

[Service]
User=root
WorkingDirectory=/etc/systemd/system/Visual-GPU/backend/
ExecStart=/home/tomo/anaconda3/envs/vig/bin/uvicorn fast:app --host 0.0.0.0 --port 8000
Restart=always
StandardOutput=file:/var/log/vig-app.log
StandardError=file:/var/log/vig-app.log

[Install]
WantedBy=multi-user.target
```

### サービスの起動
```
sudo systemctl daemon-reload
sudo systemctl start vig-app
sudo systemctl status vig-app
```

WiP
- かっこよくなってきた v3

<img width="1010" alt="Screenshot 2023-07-21 at 4 21 28" src="https://github.com/tomo-cps/Visual-GPU/assets/103920024/dbdae316-4479-4528-a46f-ebff9123bf05">

