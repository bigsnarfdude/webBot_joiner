#pip3 install pyjwt

import jwt
import hashlib
import hmac
import base64
import time
import datetime

def generateSignature(data, secret):
    encoded_jwt = jwt.encode(data, secret, algorithm="HS256")
    return (encoded_jwt);


if __name__ == '__main__':

    iat = round(datetime.datetime.now().timestamp()) - 30
    exp = iat + 60 * 60 * 2
    tokenExp = exp 
    SDK_KEY = "sdk_key"
    SDK_SECRET = "sdk_secret"
    MEETING_NUMBER = str(123456789)
    meetingNumber = 123456789
    MEETING_PASSWORD = 'Gretsky99'


    data = { "sdkKey": SDK_KEY,
             "mn": meetingNumber,
             "role": 0,
             "iat": iat, 
             "exp": exp,
             "appKey": SDK_KEY,
             "tokenExp": tokenExp
            }

    SIGNATURE = generateSignature(data, SDK_SECRET)

    print("")
    zero = '/usr/bin/open -a "/Applications/Google Chrome.app" '
    first = "'http://127.0.0.1:8888/meeting.html?name=webname&mn="
    second = '&email=&pwd='
    third = '&role=0&lang=en-US&signature='
    fourth = "&china=0&sdkKey=sdk_key'"
    text = zero+first+MEETING_NUMBER+second+MEETING_PASSWORD+third+SIGNATURE+fourth
    print(text)
    print("")
