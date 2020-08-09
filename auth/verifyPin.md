## Verify Pin
Verify Client with PIN provided in an email. Pass a consistent Client UUID at login to avoid needing to do this more than once.

`POST /api/v4/account/{AccountID}/client/{ClientID}/pin/verify`

### Headers
- **Content-Type** - `application/json`
- **TOKEN-AUTH** -  session auth token

### Parameters
- **AccountID** - Account ID
- **ClientID** - Client ID

### Body
- **pin** - PIN provided in email

### Response
- **valid** - Was the PIN accepted by Blink?


### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/api/v4/account/1234/client/1234567/pin/verify \
  --header 'content-type: application/json' \
  --header 'token-auth: {AuthToken}' \
  --data '{"pin":"123456"}'
```


### Example Response
`200 OK`

```javascript
{
  "valid": true,
  "require_new_pin": false,
  "message": "Client has been successfully verified",
  "code": 1234
}
```
