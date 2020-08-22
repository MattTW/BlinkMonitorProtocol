## Liveview

Ask for a live video stream of the given camera

`POST /api/v5/accounts/{AccountID}/networks/{NetworkID}/cameras/{CameraID}/liveview`

### Headers
- **TOKEN-AUTH** -  session auth token
- **content-type** - `application/json`

### Body
- **intent** - `liveview`
- **motion_event_start_time** - empty string = immediate?

### Response
A command object containing a Real Time Streaming Protocol (RTSP) URL 

### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/api/v5/accounts/1234/networks/1234/cameras/123456/liveview \
  --header 'content-type: application/json' \
  --header 'token-auth: {Auth-Token}' \
  --data '{"intent":"liveview","motion_event_start_time":""}'
```

### Example Response
`200 OK`

```javascript
{
  "command_id": 1234567890,
  "join_available": true,
  "join_state": "available",
  "server": "rtsps://<URL>",
  "duration": 300,
  "continue_interval": 30,
  "continue_warning": 10,
  "submit_logs": true,
  "new_command": true,
  "media_id": null,
  "options": {}
}

