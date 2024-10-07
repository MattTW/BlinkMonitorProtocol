## Set Thumbnail for Owl

Set the thumbail by taking a snapshot of the current view of the camera.

`POST /api/v1/accounts/{accountID}/networks/{NetworkID}/owls/{CameraID}/thumbnail'

/network/{NetworkID}/camera/{CameraID}/thumbnail`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
A command object.  See example.  This call is asynchronous and is monitored by the [Command Status](../network/command.md) API call using the returned Command Id.

### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/api/v1/accounts/11111/networks/22222/owls/44444/thumbnail \
  --header 'token-auth: {Auth-Token}'
```

### Example Response
`200 OK`

```javascript
{'id': 1678210511, 'network_id': 158164, 'command': 'thumbnail', 'state': 'new'}
