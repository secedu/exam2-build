# auth_2 - hidden login field
- Setup burp suite proxy to intercept requests. (intercept off for now)
- Login using ‘guest’ and ‘guest’
- Inspect the request,
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528334621247_Screenshot+2018-06-06+18.20.38.png)

- Notice the ‘role’ parameter with value ‘user’, decide to try changing this. If you inspect the cookie you may also notice the role field is included as base64 json, further motivating you to try altering this. 
![Example session cookie, after modifying the role value — which determines if user is an admin.](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528335035716_Screenshot+2018-06-06+18.29.31.png)

- Set intercept to on and login again with ‘guest’ and ‘guest’.
- In Burp, modify role=user to role=admin
- Forward the request and turn off intercept.
- Navigate to /admin to find flag{…} displayed.
- NOTE: This can also be done more simply without Burp by using Chrome to inspect/modify the hidden form field value. You could even decode, modify and encode the cookie if you want.
