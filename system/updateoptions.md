## Update Client Options
Update client specific options.   Details unknown.

`POST /client/{ClientID}/update`

### Headers
- **TOKEN-AUTH** -  session auth token

### Body
- **notification_key** - ?


### Response
- **client object** - see example

### Example Request
```sh
curl --request POST \
  --url https://rest-prod.immedia-semi.com/client/1234567/update \
  --header 'token-auth: {Auth-Token}' \
  --data '{"notification_key":"aNotificationKeyString"}'
```


### Example Response
`200 OK`

```javascript
{
  "client": {
    "id": 1234567,
    "created_at": "2019-09-20T17:59:16+00:00",
    "updated_at": "2020-08-22T12:50:31+00:00",
    "name": "",
    "notify_sound": null,
    "client_type": "ios",
    "client_specifier": " |  | 6.0.13 (8528) #df463ac0",
    "notification_key": "aNotificationKeyString",
    "aws_key": null,
    "os_version": "",
    "device_identifier": "",
    "app_version": "6.0.13 (8528) #df463ac0",
    "unique_id": "aUUIDString",
    "home": null,
    "ssid": null,
    "ssid_updated_at": "2020-08-22T12:50:31+00:00",
    "enabled_notifications": 123456789012345,
    "client_options": "aClientOptionsString",
    "verified": true,
    "user_id": 1234,
    "account_id": 1234
  }
}
```