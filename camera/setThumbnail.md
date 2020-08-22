## Set Thumbnail for Camera

Set the thumbail by taking a snapshot of the current view of the camera.

`POST /network/{NetworkID}/camera/{CameraID}/thumbnail`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
A command object.  See example.  This call is asynchronous and is monitored by the [Command Status](../network/command.md) API call using the returned Command Id.

### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/network/1234/camera/123456/thumbnail \
  --header 'token-auth: {Auth-Token}'
```

### Example Response
`200 OK`

```javascript
{
  "id": 1234567890,
  "created_at": "2020-08-22T13:09:00+00:00",
  "updated_at": "2020-08-22T13:09:00+00:00",
  "execute_time": "2020-08-22T13:09:00+00:00",
  "command": "thumbnail",
  "state_stage": "rest",
  "stage_rest": "2020-08-22T13:09:00+00:00",
  "stage_cs_db": null,
  "stage_cs_sent": null,
  "stage_sm": null,
  "stage_dev": null,
  "stage_is": null,
  "stage_lv": null,
  "stage_vs": null,
  "state_condition": "new",
  "sm_ack": null,
  "lfr_ack": null,
  "sequence": null,
  "attempts": 0,
  "transaction": "aTransactionString",
  "player_transaction": "aPlayerTransactionString",
  "server": null,
  "duration": null,
  "by_whom": " - 6.0.13 (8528) #df463ac0",
  "diagnostic": false,
  "debug": "",
  "opts_1": 0,
  "target": "camera",
  "target_id": 123456,
  "parent_command_id": null,
  "camera_id": 123456,
  "siren_id": null,
  "firmware_id": null,
  "network_id": 1234,
  "account_id": 1234,
  "sync_module_id": 123456
}

