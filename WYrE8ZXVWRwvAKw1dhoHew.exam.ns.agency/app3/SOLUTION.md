# auth_1 - base64 cookie
- Login using ‘guest’ and ‘guest’
- Inspect cookie using ‘EditThisCookie’ or whatever you’d like.
- Notice the cookie appears to be base64 - so decode it,
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528335292316_Screenshot+2018-06-06+18.34.05.png)

- Notice the username and that secret appears to be a hash.
- Calculate common hash values of things you know i.e. username (refer to auth_6 for how)
- Determine that the secret is md5(username)!
- Construct new cookie using ‘admin’ and secret of md5(‘admin’)
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528335595385_Screenshot+2018-06-06+18.39.09.png)

- Set the session cookie to this new value using ‘EditThisCookie’ or however you want.
- Refresh the page, noticing that you’re now logged in as the ‘admin’ user.
- Navigate to /admin to find flag{…} displayed.

Cookie: eyJ1c2VybmFtZSI6ICJhZG1pbiIsICJzZWNyZXQiOiAiMjEyMzJmMjk3YTU3YTVhNzQzODk0YTBlNGE4MDFmYzMifQ==
