# sql_1 - SELECT ERROR Based (no spaces)
- Go to https://box.6jlkchlgyvihgdejxoygzw.exam.ns.agency
- Inspect links for a recent trash, /`page/a98d89bb-1137-4d51-ad3b-5bbf9ed06149`
- Notice that it appears to be using UUID’s for the page lookup
- Test for SQL injection on the UUID using `/page/``'`, sure enough this dumps a SQL error
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528347591631_Screenshot+2018-06-06+21.59.20.png)

- After some playing around with the string, notice it is stripping space characters and can’t handle slashes as they would modify the URL. Using your knowledge of SQL injection and MySQL syntax, you may try encoding spaces %20 but this is also stripped.
- Instead, try using encoded tabs `%09` to space your query out. 
- Using this we get to the basic injection `/page/'%09OR%091=1%23`. Note that it was also important here to encode the ‘#’ at the end otherwise it will throw more errors. 
- NOTE: We’re nice people, so it just happens that the flag is index 0 and this payload is enough to complete the challenge. Otherwise it would require LIMIT to find the trash you wanted.
- Payload (with limit as a bonus) is as follows, `/page/'%09OR%091=1%09LIMIT%091,1%23`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528351492976_Screenshot+2018-06-06+23.04.40.png)
