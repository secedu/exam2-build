# LFI_1 - data-6.WlmGhm2kGoQyZXBTtmM8xw.exam.ns.agency (/safe/page)

The URL of the iFrame on this page points to /safe/page?p=home.html. The ‘p’ parameter of this URL is vulnerable to a local file inclusion via directory traversal. 

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528381253922_Screen+Shot+2018-06-07+at+10.43.07+pm.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528376230600_Screen+Shot+2018-06-07+at+10.44.21+pm.png)


The path `/safe/page?p=../../../flag` achieves what the user is looking for.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528376241237_Screen+Shot+2018-06-07+at+10.44.33+pm.png)
