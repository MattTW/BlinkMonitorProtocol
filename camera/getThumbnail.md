## Get Thumbnail for Camera

Retrieve the JPEG thumbnail picture of the given camera.  The URL path is specified in the thumbnail attribute of the camera, for example from the [HomeScreen](../system/homescreen.md) call.  Add the .jpg extension to the URL path.

`GET /media/production/account/{AccountId}/network/{NetworkID}/camera/{CameraId}/theClipFileName.jpg`

### Headers
- **TOKEN-AUTH** -  session auth token


### Response
`content-type: image/jpeg`

### Example Request
```sh
curl --request GET \
  --url https://rest-prod.immedia-semi.com/media/production/account/1234/network/1234/camera/123456/theClipFileName.jpg \
  --header 'token-auth: {Auth_Token}'
```


