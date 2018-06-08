## idor_3 (/message/send)
  - When sending message, change the source field to flag user `9447`. Change dest user to yourself.
  - Send a message.
  - Attached to the message should be the flag user signature which is visible

On this variant, when a user sends a message on the `/message/history` page, there is an added hidden input field called `src` which contains the user’s user ID. 

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528435197215_Screen+Shot+2018-06-08+at+3.18.27+pm.png)

If the request form were to be intercepted, modified using burp so that the `src` parameter is 9447, and the destination mailbox is the current user’s the backend will perform a message sending (from the user, to the user) with the flag included in the message content.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528435332054_Screen+Shot+2018-06-08+at+3.18.50+pm.png)
