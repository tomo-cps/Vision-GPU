# Visual-GPU
## Frontend

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