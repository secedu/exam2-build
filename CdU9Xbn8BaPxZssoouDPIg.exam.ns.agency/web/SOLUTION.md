# idor_2 - web.CdU9Xbn8BaPxZssoouDPIg.exam.ns.agency (/message/history)
  - on `/message/history?v=<B64Encrypt(mailbox)>`
  - Figure out the mailbox of the admin and the relationship between mailbox and the base64 value.

When a user has logged in, they can click on 'Messages' in the navbar to see their conversations. This page also has two iframes, where the one on the right shows a user their mailbox by supplying a base64 encoded version of their mailbox key.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528383408743_Screen+Shot+2018-06-08+at+12.40.11+am.png)


The question is what is the administrators mailbox key? The only one that has been provisioned is the greeter. If the user were to visit `/message/history?v=NGJhZGQwMGQtZDExZC00YmFkLTFkZWEtYzAwMWZhYzNkYjAx`, where the value given is the base64 encoded mailbox UUID, they would be able to see the greeter's mailbox including a discussion regarding the flag with the admin. 


![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528383437853_Screen+Shot+2018-06-08+at+12.29.29+am.png)


The important thing at this point is that the user has also obtained the mailbox key of the admin, which he can get by clicking on admin's name to populate the mailbox field. This provides the admin mailbox address: `94476441-6443-9242-6445-c001fac3d00d`.

By base64 encoding this and visiting the URL `/message/history?v=OTQ0NzY0NDEtNjQ0My05MjQyLTY0NDUtYzAwMWZhYzNkMDBk` we can now view the admin's messages and the flag.


![](https://d2mxuefqeaa7sj.cloudfront.net/s_CDBDAD1A1E89CCC50B184DFCDFAA97E7399DB0AA30A1DBB2365E916F0CCC6B11_1528383452576_Screen+Shot+2018-06-08+at+12.30.13+am.png)
