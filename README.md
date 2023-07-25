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
ex. bash setup.sh tomo anaconda3

If it doesn't work, check the port and add the following code to **/etc/init.d/my_iptables_on.sh**

```
iptables -A INPUT -p tcp --dport 8000 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 8000 -j ACCEPT
```

## Sample
![Sample](./sample/sample.gif)