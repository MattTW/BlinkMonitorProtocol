## Get Video Events

Get Media (Generally video) events since the given timestamp in the query parm.

`GET /api/v1/accounts/{AccountID}/media/changed

### Headers
- **TOKEN-AUTH** -  session auth token

### Parameters
- **since** - a timestamp to return events since.  e.g. 2020-08-03T16:50:24+0000. The official mobile client seems to use the epoch to return all available events - i.e. 1970-01-01T00:00:00+0000
- **page** - page number for multiple pages of results.

### Response
- **media** - an array of media event objects.  See example.


### Example Request
```sh
curl --request GET \
  --url 'https://rest-prod.immedia-semi.com/api/v1/accounts/1234/media/changed?since=2020-07-31T09%3A58%3A14%2B0000&page=1' \
  --header 'token-auth: {Auth_Token}'
```


### Example Response
`200 OK`

```javascript
{
  "limit": 25,
  "purge_id": 1234567890,
  "refresh_count": 0,
  "media": [
    {
      "id": 1234567890,
      "created_at": "2020-08-06T01:30:59+00:00",
      "updated_at": "2020-08-06T01:37:12+00:00",
      "deleted": false,
      "device": "camera",
      "device_id": 1234567,
      "device_name": "The Device Name",
      "network_id": 1234,
      "network_name": "The Netork Name",
      "type": "video",
      "source": "pir",
      "watched": true,
      "partial": false,
      "thumbnail": "/api/v2/accounts/1234/media/thumb/mediathumbnailname",
      "media": "/api/v2/accounts/1234/media/clip/mediavideoname.mp4",
      "additional_devices": [],
      "time_zone": "America/Chicago"
    }
  ]
}
```

