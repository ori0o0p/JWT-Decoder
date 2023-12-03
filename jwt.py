import base64
import json 

token = input() # JWT 입력 

PayloadEncoded = token.split('.')[1]

# json 형식
Payload = json.loads(
    base64.urlsafe_b64decode(PayloadEncoded + '=' * (4 - len(PayloadEncoded) % 4)))

print(Payload)