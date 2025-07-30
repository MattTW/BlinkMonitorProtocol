## Update Schedule

Update an existing schedule

`POST /api/v1/networks/{NetworkID}/programs/{ProgramID/update`

### Headers
- **TOKEN-AUTH** -  session auth token
- **content-type** - `application/json`

### Body
- **schedule object** - see example request

### Response
see example


### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/api/v1/networks/1234/programs/123/update \
  --header 'content-type: application/json' \
  --header 'token-auth: {Auth-Token}' \
  --data '{"id":123,"schedule":[{"dow":["mon","tue","wed","thu","fri"],"devices":[],"time":"2020-08-09 14:45:00 +0000","action":"arm"},{"dow":["mon","tue","wed","thu","fri"],"devices":[],"time":"2016-06-02 21:00:00 +0000","action":"disarm"}],"name":"schedulename","format":"v1"}'
```


### Example Response
`200 OK`

```javascript
{
  "program": {
    "id": 123,
    "created_at": "2016-06-02T11:49:54+00:00",
    "updated_at": "2020-08-22T12:59:41+00:00",
    "name": "schedulename",
    "data": "{\"name\":\"schedulename\",\"schedule\":[{\"dow\":[\"mon\",\"tue\",\"wed\",\"thu\",\"fri\"],\"devices\":[],\"time\":\"2020-08-09 14:45:00 +0000\",\"action\":\"arm\"},{\"dow\":[\"mon\",\"tue\",\"wed\",\"thu\",\"fri\"],\"devices\":[],\"time\":\"2016-06-02 21:00:00 +0000\",\"action\":\"disarm\"}],\"format\":\"v1\"}",
    "status": "disabled",
    "network_id": 1234,
    "user_id": 1234,
    "account_id": 1234
  },
  "actions": [
    {
      "id": 123456789,
      "created_at": "2020-08-22T12:59:41+00:00",
      "updated_at": "2020-08-22T12:59:41+00:00",
      "time": "14:45",
      "dow": "mon",
      "alt_when": null,
      "action": "arm",
      "devices": "[]",
      "status": "active",
      "last_execution": null,
      "program_id": 123,
      "network_id": 1234,
      "user_id": 1234,
      "account_id": 1234
    },
  **additional action objects corresponding to each schedule point day, action, etc**
  ]
}
```
