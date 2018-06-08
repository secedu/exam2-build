# RCE_1 - europesandbox.PolFEFBSys2GExWUGBOy-Q.exam.ns.agency (/API/list)

After inspecting the `/robots.txt` route. If the user makes a request to the `/API/list` route, it will return (conveniently) that a parameter 'v' is empty. Visiting the URL `/API/list?v=.` Will return the following output.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528381043407_Screen+Shot+2018-06-07+at+11.42.40+pm.png)


This route is vulnerable to command injection if you were to consider how one might inject a command in bash process. If we were to assume `/bin/bash /bin/ls arg` is being run, we can inject a command with the `;` character. This is not enough however, as the user must also bypass another obstacle where the argument is wrapped in `"` characters. They can get around this and perform command injection and execute `cat` by visting the URL `/API/list?v=.";cat "flag`.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528381068789_Screen+Shot+2018-06-07+at+11.43.39+pm.png)
