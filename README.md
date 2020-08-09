# BlinkMonitorProtocol
Unofficial documentation for the Client API of the Blink Wire-Free HD Home Monitoring &amp; Alert System. I am not affiliated with the company in any way - this documentation is strictly **"AS-IS"**. 

When APIs no longer appear in the current versions of the mobile Apps, we assume they are deprecated and mark them as such in this doc. PR's welcome!

The Client API is a straightforward REST API using JSON and HTTPS.

## Overview

* **Initial server URL** - https://rest-prod.immedia-semi.com
    * see [Login](auth/login.md) for notes on possible redirection to a locale specific server after login.
* **Auth Token** - Authentication is done by passing a TOKEN_AUTH header.  The auth token is provided in the response to a successful login.
* **Account** - An account corresponds to a single set of login credentials. The Account ID is returned in a successful login response.
* **Client** - A unique client/app to the account. A single account may have many client apps. Clients that the Blink servers believe are new will generate an out-of-band PIN OTP workflow.  The Client ID is returned in a successful login response.
* **Network** - A single account may have many networks. A network corresponds conceptually to a Blink Synch module. An account could have multiple networks/synch modules - e.g. multiple sites/homes. Network ID's and Synch Module information associated with an account is returned in the homescreen call.
* **Camera** - A network/synch module may have one or more cameras. Camera ID information is returned in the homescreen call.
* **Command** - Some operations reach out from the Blink Servers to your local Blink module.  These operations are asynchronous and return a Command ID to be polled for completion via the Command Status call.


### Authentication

* [Login](auth/login.md) : `POST /api/v4/account/login`
* [Logout](auth/logout.md) : `POST /api/v4/account/{AccountID}/client/{clientID}/logout`
* [Verify Pin](auth/verifyPin.md) : `POST /api/v4/account/{AccountID}/client/{ClientID}/pin/verify`


### System

* [HomeScreen](system/homescreen.md) : `GET /api/v3/accounts/{AccountID}/homescreen`
* [Get Account Notification Flags](system/getNotifications.md) : `GET /api/v1/accounts/{AccountID}/notifications/configuration`
* Set Notification Flags : `POST /api/v1/accounts/{AccountID}/notifications/configuration`
* [General Client Options](system/options.md) : `GET /api/v1/accounts/{AccountID}/clients/{ClientID}/options`


### Network

* Command Status : `GET /network/{NetworkID}/command/{CommandID}`
* Arm System : `POST /api/v1/accounts/{AccountID}/networks/{NetworkID}/state/arm`
* Disarm System : `POST api/v1/accounts/{AccountID}/networks/{NetworkID}/state/disarm`
* [List Schedules](network/listPrograms.md) : `GET /api/v1/networks/{NetworkID}/programs`
* Enable Network Program : `POST /api/v1/networks/{NetworkID}/programs/{ProgramID}/enable`
* Disable Network Program : `POST /api/v1/networks/{NetworkID}/programs/{ProgramID}/disable`
* List Networks (deprecated? - replaced by HomeScreen): `GET /networks`
* List Synch Modules (deprecated? - replaced by HomeScreen) `GET /network/{NetworkID}/syncmodules`


### Cameras

* Enable Motion Detection : `POST /network/{NetworkID}/camera/{CameraID}/enable` *Note*: No motion detection or video recording will take place unless the system is armed.
* Disable Motion Detection : `POST /network/{NetworkID}/camera/{CameraID}/disable`
* [Get Current Thumbnail](camera/getThumbnail.md) : `GET /media/production/account/{AccountID}/network/{NetworkID}/camera/{CameraID}/{JPEG_File_Name}.jpg`
* Create New Thumbnail : `POST /network/{NetworkID}/camera/{CameraID}/thumbnail`
* Liveview : `POST /api/v5/accounts/{AccountID}/networks/{NetworkID}/cameras/{CameraID}/liveview`
* Get Camera Config : `GET /network/{NetworkID}/camera/{CameraID}/config`
* Update Camera Config : `POST /network/{NetworkID}/camera/{CameraID}/update`
* Get Camera List (deprecated? - replaced by HomeScreen) - `GET /network/{NetworkID}/cameras`
* Get Camera Info (deprecated? - replaced by HomeScreen) - `GET /network/{NetworkID}/camera/{CameraID}`
* Get Camera Sensor Info (deprecated? - replaced by HomeScreen) - `GET /network/{NetworkID}/camera/{CameraID/signals`


### Videos

* [Get Video Events](videos/getVideoEvents.md) : `GET /api/v1/accounts/{AccountID}/media/changed?since={timestamp}&page={PageNumber}`
* Get Video : `GET /api/v2/accounts/{AccountID}/media/clip/{mp4_Filename}`
* Get Video Thumbnail:  
* Set Video Thumbnail: 
* Set Video Options : `POST /api/v1/account/video_options`
* Get Network events (deprecated? replaced by Get Video Events) - `GET /events/network/{NetworkID}`
* Get Video Count (deprecated?) - `GET /api/v2/videos/count`
* Get Video Info by Page (deprecated?) - `GET /api/v2/videos/page/{PageNumber}`
* Get Video by ID (deprecated?) - `GET /api/v2/video/{VideoID}`
* Get Unwatched Videos (deprecated?) - `GET /api/v2/videos/unwatched`
* Delete a Video (deprecated?) - `GET /api/v2/video/{VideoID}/delete`
* Delete all Videos (deprecated?) - `GET /api/v2/videos/deleteall`


### Misc

* [App Version Check](misc/version.md) : `GET /api/v1/version`
* [Get Regions](misc/regions.md) : `GET /regions?locale={Two Character Country Locale}`
* Upload Logs : `POST /app/logs/upload`
* [Account Options](misc/accountOptions.md) : `GET /api/v1/account/options`
* System Health (deprecated?) `GET /health`
* Clients (deprecated?) `GET /account/clients`
