# LFI_2 - login.box.6JlKchlgYViHgDeJxoYgzw.exam.ns.agency (/safe/doc)

When a user navigates to the bottom of the page being served up by the iFrame, they will find a link to another page '/safe/page?p=articles.html'. Whilst the page parameter is not vulnerable anymore, if a user were to investigate the source code of this page, they will find that the documents are loaded by another route `/safe/doc?d=malloc_maleficarum.txt`.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528380928371_Screen+Shot+2018-06-07+at+11.02.13+pm.png)


This document loader is exploitable by directory traversal to perform local file inclusion. To achieve the flag, users visit `/safe/doc?d=../../../flag`.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528380952893_Screen+Shot+2018-06-07+at+11.02.43+pm.png)
