## Disarm the System

Disarm the given network - that is, stop recording/reporting motion events for enabled cameras.

When this call returns, it does not mean the arm request is complete,  the client must gather the command ID from the response and poll for the status of the command.
 

`POST api/v1/accounts/{AccountID}/networks/{NetworkID}/state/disarm`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
- A command object.  See example.  This call is asynchronous and is monitored by the [Command Status](../network/command.md) API call using the returned Command Id.

### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/api/v1/accounts/1234/networks/1234/state/disarm \
  --header 'token-auth: {Auth_Token}'
```

### Example Response
`200 OK`

```javascript
{
  "id": 123456789,
  "network_id": 1234,
  "command": "disarm",
  "state": "new",
  "commands": [
    {
      "id": 123456780,
      "network_id": 1234,
      "command": "config_lfr",
      "state": "running"
    },
    {
      "id": 123456781,
      "network_id": 1234,
      "command": "config_lfr",
      "state": "running"
    }
  ]
}



