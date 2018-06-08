## LFI_3 - (/safe/img)

When a user views the source code of `safe/page?p=home.html`, `safe/page?p=articles.html` they will find that the images are being served up by the route `safe/img`. In a similar fashion to the other two instances, this can be exploited by local file inclusion. The route `/safe/img?i=../../../flag` will allow a user to download the flag from the server as if it were an image.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528380978586_Screen+Shot+2018-06-07+at+11.23.50+pm.png)
