## Login
Client Login to Blink Account on Blink Servers

`POST /api/v5/account/login`

### Headers
- **Content-Type** -  `application/json`

### Body
- **email** - Account userid/email
- **password** - Account password
- **unique_id** - (optional) UUID generated and identifying the client.  Pass a consistent value here to avoid repeated client verification PIN requests.

### Response
- **account&#46;account_id** - Account Identifier 
- **account&#46;client_id** - Client Identifier
- **account&#46;client_verification_required** - Client verification required by Blink Servers, see [Verify Pin](verifyPin.md).
- **auth&#46;token** - String Authentication token to be passed as `TOKEN_AUTH` header in future calls
- **account&#46;tier** - Tier (see notes below)

### Notes
Depending on where your Blink system is registered, the tier info appears necessary to form the localized URL of the REST endpoint for future calls. Current logic seems to be to update the REST endpoint using region.tier data in the response:
- from `https://rest-prod.immedia-semi.com`
- to `https://rest-{account.tier}.immedia-semi.com` Reports indicate that all regions are not implemented equally, i.e. not all endpoints are available in all regions

### Example Request
```sh
curl 'https://rest-prod.immedia-semi.com/api/v5/account/login' -X POST  -H 'Content-Type: application/json' -d '{"unique_id": "00000000-0000-0000-0000-000000000000", "password":"aPassword","email":"anEmail"}'
```


### Example Response
`200 OK`

```javascript
{
    "account": {
        "account_id": 1234,
        "user_id": 123456,
        "client_id": 1234567,
        "new_account": false,
        "tier": "e002",
        "region": "eu",
        "account_verification_required": false,
        "phone_verification_required": false,
        "client_verification_required": false,
        "verification_channel": "phone"
    },
    "auth": {
        "token": "anAuthTokenString"
    },
    "phone": {
        "number": "+49*******1234",
        "last_4_digits": "1234",
        "country_calling_code": "49",
        "valid": true
    },
    "verification": {
        "email": {
            "required": false
        },
        "phone": {
            "required": true,
            "channel": "sms"
        }
    },
    "lockout_time_remaining": 0,
    "force_password_reset": false,
    "allow_pin_resend_seconds": 60
}
```
