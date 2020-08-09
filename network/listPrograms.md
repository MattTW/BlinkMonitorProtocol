## List Schedules

List the schedules (programs) defined for the given Network/Blink Module

`GET /api/v1/networks/{NetworkID}/programs`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
An array of program objects - see example


### Example Request
```sh
curl --request GET \
  --url https://rest-prod.immedia-semi.com/api/v1/networks/1234/programs \
  --header 'token-auth: {Auth_Token}'
```


### Example Response
`200 OK`

```javascript
[
  {
    "id": 123,
    "network_id": 1234,
    "status": "disabled",
    "name": "Schedule Name",
    "schedule": [
      {
        "dow": [
          "mon",
          "tue",
          "wed",
          "thu",
          "fri"
        ],
        "devices": [],
        "time": "2016-06-02 14:45:00 +0000",
        "action": "arm"
      },
      {
        "dow": [
          "mon",
          "tue",
          "wed",
          "thu",
          "fri"
        ],
        "devices": [],
        "time": "2016-06-02 21:00:00 +0000",
        "action": "disarm"
      }
    ],
    "format": "v1"
  }
]
```