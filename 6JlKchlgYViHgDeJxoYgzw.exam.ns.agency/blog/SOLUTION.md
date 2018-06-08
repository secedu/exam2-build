# idor_1 - blog.6JlKchlgYViHgDeJxoYgzw.exam.ns.agency (/user/9447)
  - on `/user/<int:userid>`
  - IDOR to the flag user. Flag user ID should be 9447
![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528383313709_Screen+Shot+2018-06-08+at+12.25.19+am.png)


When a user has logged in, they are shown a window with two iFrames. The iframe on the left is exploitable through an insecure direct object reference in the route. If a user were to provide `/user/9447` they would output the credentials of the admin account and find the flag in the signature.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528383359749_Screen+Shot+2018-06-08+at+12.25.55+am.png)
