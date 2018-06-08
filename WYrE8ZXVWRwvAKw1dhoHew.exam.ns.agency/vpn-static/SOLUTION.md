# idor_4 - (/modify/9447)
  - access `/modify/<int:userid>` for another user
  - view the flag in their signature.

When a user logs in for the first time, they are given an iframe that allows them to modify their credentials. This is at the route `/modify/<int:userid>` If the user were to change the integer value in the route to 9447, they would be able to read the first name, lastname and signature of the admin account.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528383496353_Screen+Shot+2018-06-08+at+12.27.00+am.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528433908746_Screen+Shot+2018-06-08+at+2.57.56+pm.png)
