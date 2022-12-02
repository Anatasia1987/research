a = int(input ('Enter password :'))
if a==1234:
    b = int(input('Enter New Password:'))
    c = int(input('Confirm New Password:'))
    if b == c:
        print ('Your Password Has Changed Successfully')
    else:
        print ('This Password is not Confirmed')
else:
    print ('Unauthorised access')
    