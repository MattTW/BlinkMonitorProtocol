## Command Status

Return the status of the given command.

Most Camera and System/Module APIs make a call from the Blink Server to your local Synch Module.  These calls are asynchronous and return a command object.  Use the returned command id in these calls to poll for completion of the command using this API until the `complete` flag is true in the response.

The mobile clients poll for completion approximately once a second.

`GET /network/{NetworkID}/command/{CommandID}`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
An array of program objects - see example


### Example Request
```sh
curl --request GET \
  --url https://rest-prod.immedia-semi.com/network/1234/command/123456789 \
  --header 'token-auth: {Auth_Token}'
```


### Example Response
`200 OK`

```javascript
{
  "complete": true,
  "status": 0,
  "status_msg": "Command succeeded",
  "status_code": 908,
  "commands": [
    {
      <<the original command object>>
    }
  ],
  "media_id": null
}
```