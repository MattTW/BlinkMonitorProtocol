## Login
Retrieve Client "home screen" data.  Returns detailed information about the Account including Network, Synch Module, and Camera Info.

`GET /api/v3/accounts/{AccountID}/homescreen`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
See example


### Example Request
```sh
curl --request GET \
  --url https://rest-prod.immedia-semi.com/api/v3/accounts/1234/homescreen \
  --header 'token-auth: {AuthToken}'
```


### Example Response
`200 OK`

```javascript
{
  "account": {
    "id": 1234,
    "email_verified": true,
    "email_verification_required": false
  },
  "networks": [
    {
      "id": 5678,
      "created_at": "2016-01-03T22:37:59+00:00",
      "updated_at": "2020-08-03T22:37:50+00:00",
      "name": "Network-Name",
      "time_zone": "America/Chicago",
      "dst": true,
      "armed": true,
      "lv_save": false
    }
  ],
  "sync_modules": [
    {
      "id": 123456,
      "created_at": "2017-09-16T15:45:36+00:00",
      "updated_at": "2020-08-09T00:00:31+00:00",
      "onboarded": true,
      "status": "online",
      "name": "My Blink Sync Module",
      "serial": "123456789",
      "fw_version": "2.13.26",
      "last_hb": "2020-08-09T14:14:13+00:00",
      "wifi_strength": 5,
      "network_id": 5678,
      "enable_temp_alerts": true
    }
  ],
  "cameras": [
    {
      "id": 1234,
      "created_at": "2016-01-03T23:15:42+00:00",
      "updated_at": "2020-08-09T13:02:14+00:00",
      "name": "Camera Name",
      "serial": "123456789"
      "fw_version": "2.151",
      "type": "white",
      "enabled": false,
      "thumbnail": "/media/production/account/1234/network/5678/camera/1234/clip_name",
      "status": "done",
      "battery": "ok",
      "usage_rate": true,
      "network_id": 5678,
      "issues": [],
      "signals": {
        "lfr": 3,
        "wifi": 5,
        "temp": 68,
        "battery": 3
      }
    },
    {
      "id": 123456,
      "created_at": "2017-04-30T16:31:24+00:00",
      "updated_at": "2020-07-31T11:32:14+00:00",
      "name": "Camera Name",
      "serial": "123456789",
      "fw_version": "2.151",
      "type": "xt",
      "enabled": true,
      "thumbnail": "/media/production/account/1234/network/5678/camera/123456/clip_name",
      "status": "offline",
      "battery": "low",
      "usage_rate": false,
      "network_id": 5678,
      "issues": [],
      "signals": {
        "lfr": 5,
        "wifi": 1,
        "temp": 75,
        "battery": 3
      }
    }
  ],
  "sirens": [],
  "chimes": [],
  "video_stats": {
    "storage": 1,
    "auto_delete_days": 7
  },
  "doorbell_buttons": [],
  "owls": [],
  "app_updates": {
    "message": "An app update is required",
    "code": 105,
    "update_available": true,
    "update_required": true
  },
  "device_limits": {
    "camera": 10,
    "chime": 5,
    "doorbell_button": 2,
    "owl": 10,
    "siren": 5,
    "total_devices": 20
  },
  "whats_new": {
    "updated_at": 20200622,
    "url": "https://blinkforhome.com/blogs/updates"
  }
}
```