# auth_6 - session cookie sha1(username)
- Login using username, password ‘guest’ and ‘guest’. 
- Inspect cookie using something like ‘EditThisCookie’ or any method you’re used to.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528331821059_Screenshot+2018-06-06+17.36.44.png)

- Notice that it appears to be a hash.
- Decide to try hashing the username/password for the account using common hashes.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528331937308_Screenshot+2018-06-06+17.38.43.png)

- Calculate hash for username ‘admin’
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528331972781_Screenshot+2018-06-06+17.39.17.png)

- Set new session cookie value using ‘EditThisCookie’ or any other method.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528332106498_Screenshot+2018-06-06+17.40.04.png)

- Refresh the page, noticing that you’re now logged in as the ‘admin’ user.
- Navigate to /admin to find flag{…} displayed.
