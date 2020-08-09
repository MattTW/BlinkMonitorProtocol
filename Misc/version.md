## App Version Check
Determine if a new version of the official client is available.  This call does not require authentiation.  This information is also returned in the [HomeScreen](../system/homesceen.md) call.

`GET /api/v1/version`

### Headers
- **APP-BUILD** -  The client build string as specified by the mobile client. e.g. `IOS_8528`


### Response
see example

### Example Request
```sh
curl --request GET \
  --url https://rest-prod.immedia-semi.com/api/v1/version \
  --header 'app-build: IOS_8528'
```


### Example Response
`200 OK`

```javascript
{
  "message": "OK",
  "code": 103,
  "update_available": false,
  "update_required": false
}
```