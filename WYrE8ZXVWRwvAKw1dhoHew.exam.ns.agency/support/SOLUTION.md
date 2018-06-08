# sql_2 - SELECT ERROR Based (blacklist chars)
- Here we notice that we can’t seem to escape out using single quotes anymore. This may tingle our spider sense that perhaps they’re being escaped with backslashes. (This is right!)
- If we add an encoded backslash before our basic payload we get  `/page/%5c'%20OR%201=1%23`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528351415113_Screenshot+2018-06-06+23.03.25.png)
