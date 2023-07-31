# Visual-GPU
## Frontend

This repository is an application that can visualize GPU availability！
The backend is created in Python and the frontend in Vue3.js Vuetify3.

```
npm install 
```

```
npm run serve
```

## Backend

```
bash setup.sh USER_NAME YOUR_PYTHON_SOFTWARE
```
ex. bash setup.sh tomo [anaconda3](https://www.anaconda.com/download/)

If it doesn't work, check the port and add the following code to **/etc/init.d/my_iptables_on.sh**

```
iptables -A INPUT -p tcp --dport 8000 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 8000 -j ACCEPT
```
## Sample Image
<img width="1217" alt="Screenshot 2023-07-31 at 15 54 07" src="https://github.com/tomo-cps/Visual-GPU/assets/103920024/c4274c10-39fa-465d-8db9-a6393408df25">

## Sample Gif
![Sample](./sample/sample.gif)
