# auth_5 - multistep bypass
- Go to https://6preview.6jlkchlgyvihgdejxoygzw.exam.ns.agency
- Click ‘RESET PASSWORD’
- Enter ‘guest’ as username and click ‘SUBMIT’
- Enter guest’s secret answer, ‘unsw’ and enter a new password of your choice but don’t submit.
- Now we modify the hidden ‘username’ form field from ‘guest’ to ‘admin’ and click ‘SUBMIT’.
![](https://d2mxuefqeaa7sj.cloudfront.net/s_D1CF04A7F2975FBE28B89C00E052CDE16A28AD0D6622A39C029738E493BE6857_1528400623220_Screenshot+2018-06-07+12.42.44.png)

- Should see ‘Password Reset Successful’ which means we’ve now reset the admin’s password!
- Login using ‘admin’ and your new password.
- Navigate to /admin to find flag{…} displayed.
