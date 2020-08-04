# BlinkMonitorProtocol
Unofficial documentation for the Client API of the Blink Wire-Free HD Home Monitoring &amp; Alert System.

I am not affiliated with the company in any way - this documentation is strictly **"AS-IS"**. 

Blink/Amazon appears to keep previous versions of APIs running until mobile clients are forced to upgrade - APIs can and have been obsoleted.  As unofficial doc, we get no deprecation warning.  When APIs no longer appear in the current versions of the mobile Apps, we assume they are deprecated and mark them as such in this doc. PR's welcome!  

## Overview

* Initial server URL:  https://rest-prod.immedia-semi.com
    * see [Login](authentication.md) for notes on possible redirection to a locale specific server after login.
* **Auth Token** - authentication of API calls is done by passing a TOKEN_AUTH header.  The auth token is provided in the response to a successful login.
* **Account** - An account corresponds to a single set of login credentials. The AccountID is returned in a successful login response.
* **Client** - a unique client/app to the account. A single account may have many client apps. Clients determined as new by Blink will generate an out of band PIN OTP workflow.  The clientID is returned in a successful login response.
* **Network** - A single account may have many networks. A network corresponds conceptually to a Blink Synch module. An account could have multiple networks/synch modules - e.g. multiple sites/homes. Network ID's and Synch Module information associated with an account is currently returned in the homescreen call.
* **Camera** A network/synch module may have one or more cameras. Camera ID information is currently returned in the homescreen call.


### Authentication

* [Login](auth/login.md) : `POST /api/v4/account/login`
* [Logout](auth/logout.md) : `POST /api/v4/account/{$AccountID}/client/{$clientID}/logout`
* Verify Pin : `POST /api/v4/account/${AccountID}/client/{$ClientID}/pin/verify`


### System

* HomeScreen : `GET /api/v3/accounts/{$AccountID}/homescreen`
* General Client Options : `GET /api/v1/accounts/{$AccountID}/clients/{$ClientID}/options`
* Get Notification Flags : `GET /api/v1/accounts/{$AccountID}/notifications/configuration`
* Set Notification Flags : `POST /api/v1/accounts/{$AccountID}/notifications/configuration`


### Network

A Network corresponds conceptually to individual Synch modules. A single account could have multiple networks/modules (e.g. multiple sites/homes)

Generally speaking, commands specific to a network are reaching out to your Blink module to issue the commad and wait for a response, these calls are asynchronous and clients must poll to wait for a response via the Command Status call.

* Command Status : `GET /network/{$NetworkID}/command/{$CommandID}`
* Arm System : `POST /api/v1/accounts/{$AccountID}/networks/{$NetworkID}/state/arm`
* Disarm System : `POST api/v1/accounts/{$AccountID}/networks/{$NetworkID}/state/disarm`
* List Network Programs : `GET /api/v1/networks/{$NetworkID}/programs`
* Enable Network Program : `POST /api/v1/networks/{$NetworkID}/programs/{$ProgramID}/enable`
* Disable Network Program : `POST /api/v1/networks/{$NetworkID}/programs/{$ProgramID}/disable`

### Cameras

As with Network calls, these calls are sent to your Blink module by Blink's server and are asynchronous - they must be polled for completion with the Command Status call.

* Enable Motion Detection : `POST /network/{$NetworkID}/camera/{$CameraID}/enable`
* Disable Motion Detection : `POST /network/{$NetworkID}/camera/{$CameraID}/disable`
* Get Current Thumbnail : `GET /media/production/account/{$AccountID}/network/{$NetworkID}/camera/{$CameraID}/{$JPEG_File_Name}`
* Create New Thumbnail : `POST /network/{$NetworkID}/camera/${CameraID}/thumbnail`
* Liveview : `POST /api/v5/accounts/{$AccountID}/networks/{$NetworkID}/cameras/{$CameraID}/liveview`
* Get Camera Config : `GET /network/{$NetworkID}/camera/{$CameraID}/config`
* Update Camera Config : `POST /network/{$NetworkID}/camera/{$CameraID}/update`
* Capture Clip - deprecated?
* Camera Signals (battery, wifi, etc) - deprecated?

### Videos

Videos are stored on Blink's servers, therefore they are synchronous and do not have to be polled.

* Get Media events ("changed since" filter) : `GET /api/v1/accounts/{$AccountID}/media/changed` (?since=2020-08-03T16:50:24+0000&page=1) (?since=1970-01-01T00:00:00+0000&page=1)
* Get Media video clip : `GET /api/v2/accounts/{$AccountID}/media/clip/{$mp4_Filename}`
* Video Options : `POST /api/v1/account/video_options`
* Get Network events - deprecated?
* Paginated list, etc - deprecated?


### Misc

* Version : `GET /api/v1/version`
* Regions : `GET /regions` (?locale=US)
* Upload Logs : `POST /app/logs/upload`
* Mystery Options Call : `GET /api/v1/account/options`
* Networks - deprecated?
* Synch Modules - deprecated?
* System Health - deprecated?
* Clients - deprecated? 



## Login

Client login to the Blink Servers.

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "Content-Type: application/json" --data-binary '{
>  "password" : "*your blink password*",
>  "client_specifier" : "iPhone 9.2 | 2.2 | 222",
>  "email" : "*your blink login/email*"
>}' --compressed https://rest-prod.immedia-semi.com/api/v4/account/login

**Response:**
>{ "account": { "id": "*an account number*" },
"client": { "id" : "*a client id*" },
"authtoken":{"authtoken":"*an auth token*","message":"auth"},"networks":{"*network id*":{"name":"*name*","onboarded":true}},"region":{"*regioncode for endpoint*":"*region name"}}

**Notes:**
The authtoken value is passed in a header in future calls.
The region code for endpoint is required to form the URL of the REST endpoint for future calls.
Depending on the region you are registered you will need to change the REST endpoints below:
- from `https://rest.prod.immedia-semi.com`
- to `https://rest.prde.immedia-semi.com` if e.g. your device is registered in Germany
Please note that at this moment it seems that all regions are not implemented equally: not all endpoints are available in all regions

## Networks

Obtain information about the Blink networks defined for the logged in user.

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/networks

**Response:**
JSON response containing information including Network ID and Account ID.

**Notes:**
Network ID is needed to issue arm/disarm calls


## Sync Modules

Obtain information about the Blink Sync Modules on the given network.

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/network/*network_id_from_networks_call*/syncmodules

**Response:**
JSON response containing information about the known state of the Sync module, most notably if it is online

**Notes:**
Probably not strictly needed but checking result can verify that the sync module is online and will respond to requests to arm/disarm, etc.


## Arm
 
Arm the given network (start recording/reporting motion events)

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --data-binary --compressed https://rest.prod.immedia-semi.com/network/*network_id_from_networks_call*/arm

**Response:**
JSON response containing information about the arm command request, including the command/request ID

**Notes:**
When this call returns, it does not mean the arm request is complete,  the client must gather the request ID from the response and poll for the status of the command.

## Disarm

Disarm the given network (stop recording/reporting motion events)

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --data-binary --compressed https://rest.prod.immedia-semi.com/network/*network_id_from_networks_call*/disarm

**Response:**
JSON response containing information about the disarm command request, including the command/request ID

**Notes:**
When this call returns, it does not mean the disarm request is complete,  the client must gather the request ID from the response and poll for the status of the command.


## Command Status

Get status info on the given command

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/network/*network_id*/command/*command_id*

**Response:**
JSON response containing state information of the given command, most notably whether it has completed and was successful.

**Notes:**
After an arm/disarm command, the client appears to poll this URL every second or so until the response indicates the command is complete.

**Known Commands:**
lv_relay, arm, disarm, thumbnail, clip

## Home Screen

Return information displayed on the home screen of the mobile client - supports multiple sync modules.

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/network/*network_id_from_networks_call*/homescreen

**Response:**
JSON response containing information that the mobile client displays on the home page for the requested sync module, including:  status, armed state, links to thumbnails for each camera, etc.

**Notes:**
Not necessary to as part of issuing arm/disarm commands, but contains good summary info.

## Events, thumbnails & video captures

**Request**
Get events for a given network (sync module) -- Need network ID from home 

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/events/network/*network__id*

**Response**
A json list of evets incluing URL's.   Replace the "mp4" with "jpg" extension to get the thumbnail of each clip


**Request**
Get a video clip from the events list

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed **video url from events list.mp4** > video.mp4

**Response**
The mp4 video

**Request**
Get a thumbnail from the events list

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed **video url from events list.jpg** > video_thumb.jpg

**Response**
The jpg bytes. 

**Notes**
Note that you replace the 'mp4' with a 'jpg' to get the thumbnail

**Request**
Captures a new thumbnail for a camera

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --data-binary --compressed https://rest.prod.immedia-semi.com/network/*network_id*/camera/*camera_id*/thumbnail

**Response**
Command information. 

**Request**
Captures a new video for a camera

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --data-binary --compressed https://rest.prod.immedia-semi.com/network/*network_id*/camera/*camera_id*/clip

**Response**
Command information.

## Video Information

**Request**
Get the total number of videos in the system

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/api/v2/videos/count

**Response**
JSON response containing the total video count.

**Request**
Gets a paginated set of video information

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/api/v2/videos/page/0

**Response**
JSON response containing a set of video information, including: camera name, creation time, thumbnail URI, size, length

**Request**
Gets information for a specific video by ID

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/api/v2/video/*video_id*

**Response**
JSON response containing video information

**Request**
Gets a list of unwatched videos

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/api/v2/videos/unwatched

**Response**
JSON response containing unwatched video information

**Request**
Deletes a video

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --data-binary --compressed https://rest.prod.immedia-semi.com/api/v2/video/*video_id*/delete

**Response**
Unknown - not tested

**Request**
Deletes all videos

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --data-binary --compressed https://rest.prod.immedia-semi.com/api/v2/videos/deleteall

**Response**
Unknown - not tested

## Cameras

**Request**
Gets a list of cameras

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/network/*network_id*/cameras

**Response**
JSON response containing camera information

**Request**
Gets information for one camera

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/network/*network_id*/camera/*camera_id*

**Response**
JSON response containing camera information

**Request**
Gets camera sensor information

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/network/*network_id*/camera/*camera_id*/signals

**Response**
JSON response containing camera sensor information, such as wifi strength, temperature, and battery level

**Request**
Enables motion detection for one camera

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: $auth_token" --data-binary --compressed https://rest.prod.immedia-semi.com/network/*network_id*/camera/*camera_id*/enable

**Response**
JSON response containing camera information

**Request**
Disables motion detection for one camera

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: $auth_token" --data-binary --compressed https://rest.prod.immedia-semi.com/network/*network_id*/camera/*camera_id*/disable

**Response**
JSON response containing camera information

*Note*: enabling or disabling motion detection is independent of arming or disarming the system.  No motion detection or video recording will take place unless the system is armed.


## Miscellaneous

**Request**
Gets information about devices that have connected to the blink service

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/account/clients

**Response**
JSON response containing client information, including: type, name, connection time, user ID

**Request**
Gets information about supported regions

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/regions

**Response**
JSON response containing region information

**Request**
Gets information about system health

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/health

**Response**
"all ports tested are open"

**Request**
Gets information about programs

>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://rest.prod.immedia-semi.com/api/v1/networks/*network_id*/programs

**Response**
Unknown.
