# JWT-Decoder

```
import base64
import json 

token = input()

PayloadEncoded = token.split('.')[1]

Payload = json.loads(base64.urlsafe_b64decode(PayloadEncoded + '=' * (4 - len(PayloadEncoded) % 4)))

print(Payload)
```

사용자가 입력한 JWT의 페이로드를 가져와 디코딩을 하는 파이썬 코드이다. 
