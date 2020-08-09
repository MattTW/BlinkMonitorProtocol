## Client Options
Purpose Unknown

`GET /api/v1/accounts/{AccountID}/clients/{ClientID}/options`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
- **options** - specific meaning unknown

### Example Request
```sh
curl --request GET \
  --url https://rest-prod.immedia-semi.com/api/v1/accounts/1234/clients/1234567/options \
  --header 'token-auth: {Auth_Token}'
```


### Example Response
`200 OK`

```javascript
{
  "options": "A_LONG_ALPHANUMERIC_STRING"
}
```