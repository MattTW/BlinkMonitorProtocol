## Snooze Camera

Snooze (temporarily disable) motion-activated notifications for a camera.

`POST /api/v1/accounts/{AccountID}/networks/{NetworkID}/cameras/{CameraID}/snooze`

### Headers
- **TOKEN-AUTH** -  session auth token

### Body
- **snooze_time** - number of minutes, i.e. 240

### Response
Unknown

### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/api/v1/accounts/1234567/networks/1234/cameras/123456/snooze \
  --header 'token-auth: {Auth_Token}' \
  --data '{"snooze_time": 240}'
```

### Example Response
