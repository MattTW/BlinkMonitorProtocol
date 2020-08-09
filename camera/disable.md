## Disable Motion Detection for Camera

Disable motion detection for the given Camera.  

`POST /network/{NetworkID}/camera/{CameraID}/disable`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
- A command object.  See example.  This call is asynchronous and is monitored by the [Command Status](../network/command.md) API call using the returned Command Id.

### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/network/1836/camera/2381/disable \
  --header 'token-auth: {Auth_Token}'
```

### Example Response
`200 OK`

```javascript
{
  "id": 123456789,
  "created_at": "2020-08-09T22:20:16+00:00",
  "updated_at": "2020-08-09T22:20:16+00:00",
  "execute_time": "2020-08-09T22:20:16+00:00",
  "command": "config_lfr",
  "state_stage": "rest",
  "stage_rest": "2020-08-09T22:20:16+00:00",
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
  "transaction": "aTransactionID",
  "player_transaction": "aPlayTransactionID",
  "server": null,
  "duration": null,
  "by_whom": "device name - client version - unique hash",
  "diagnostic": false,
  "debug": "",
  "opts_1": 0,
  "target": "camera",
  "target_id": 5678,
  "parent_command_id": null,
  "camera_id": 5678,
  "siren_id": null,
  "firmware_id": null,
  "network_id": 1234,
  "account_id": 1234,
  "sync_module_id": 123456
}



