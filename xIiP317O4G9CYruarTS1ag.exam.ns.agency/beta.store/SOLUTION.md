# privesc_1 - beta.store.xIiP317O4G9CYruarTS1ag.exam.ns.agency (/register)

If the user successfully registers, they will find the entire app to work as intended with no planned vulnerabilities in it. Eventually this -should- push the user to investigate the registration system, where they will find a hidden input parameter called `type` which has a default value of `user`. 


![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528434535214_Screen+Shot+2018-06-08+at+3.07.17+pm.png)


By setting the default value to `admin` the flag will be returned immediately after registration as a flashed message (where it otherwise would say ‘Registration Successful’)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528434581449_Screen+Shot+2018-06-08+at+3.08.07+pm.png)

- Bonus Variant 5 - Brute force IDOR Bonus Flag
   - Discover the account username of user id `6443`. This requires the user to brute force through the user ids of the `/whois` route. ID is a special allocated ID, with all new accounts beginning from `13337`.


![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528383548482_Screen+Shot+2018-06-08+at+12.58.50+am.png)
