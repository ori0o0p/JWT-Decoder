# JWT-Decoder

```
import base64
import json 

token = input()

PayloadEncoded = token.split('.')[1]

Payload = json.loads(base64.urlsafe_b64decode(PayloadEncoded + '=' * (4 - len(PayloadEncoded) % 4)))

print(Payload)
```

