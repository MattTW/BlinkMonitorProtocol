## Logout
Client Logout Blink Account on Blink Servers

`POST /api/v4/account/{AccountID}/client/{clientID}/logout`

### Headers
- **TOKEN-AUTH** -  session auth token

### Parameters
- **AccountID** - Account ID
- **ClientID** - Client ID

### Example Request
```sh
curl 'https://rest-prod.immedia-semi.com/api/v4/account/1234/client/1234567/logout' \
-X POST \
-H 'TOKEN-AUTH: {AuthToken}'
```


### Example Response
`200 OK`

```javascript
{
  "message": "logout"
}
```
