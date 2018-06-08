# sql_4 - INSERT ERROR Based (title field)

- This time things are a little different, the UUID parameter is no longer vulnerable and if we try to mess with it we will get a friendly recommendation to try inserting some trash instead.
- We try basic single quote injection in the title and receive an error. We’re on the right track.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528354585821_Screenshot+2018-06-06+23.54.50.png)

- We could assume that the insert query uses title/content/password in that order since it’s how it’s presented on the page, but we would also find this out along the way. So we construct a payload that creates empty string for the title, somehow selects our flag into the content and then closes out insert query in a valid manner.
- In MySQL this payload is `',(SELECT GROUP_CONCAT(content) from trash as c),'')#` 
- We use this payload as the title for a new trash, 
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528354397867_Screenshot+2018-06-06+23.52.05.png)

- And we are rewarded with our booty!
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528354405924_Screenshot+2018-06-06+23.52.12.png)
