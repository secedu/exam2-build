# sql_5 - SELECT ERROR Based (only hex/symbols characters)
- It seems to be filtering all non-hex or symbol characters. We can get around this a number of ways, but the simplest is to use the ‘||’ symbols.
- Payload is `/page/'%20%7C%7C%201%20%23`
- NOTE: It is also possible to use hex encoded strings in MySQL, but it isn’t required.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528355436593_Screenshot+2018-06-07+00.10.21.png)
