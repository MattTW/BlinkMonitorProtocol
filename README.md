# BlinkMonitorProtocol
Unofficial documentation for the Client API of the Blink Wire-Free HD Home Monitoring &amp; Alert System.

I am not affiliated with the company in any way - this documentation is strictly **"AS-IS"**.  My goal was to uncover enough to arm and disarm the system programatically so that I can issue those commands in sync with my home alarm system arm/disarm.  Just some raw notes at this point but should be enough for creating programmatic APIs.    Lots more to be discovered and documented - feel free to contribute!

The Client API is a straightforward REST API using JSON and HTTPS.

##Login

Client login to the Blink Servers.

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "Content-Type: application/json" --data-binary '{
>  "password" : "*your blink password*",
>  "client_specifier" : "iPhone 9.2 | 2.2 | 222",
>  "email" : "*your blink login/email*"
>}' --compressed https://prod.immedia-semi.com/login

**Response:**
>{"authtoken":{"authtoken":"*an auth token*","message":"auth"}}

**Notes:**
The authtoken value is passed in a header in future calls.

##Networks

Obtain information about the Blink networks defined for the logged in user.

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://prod.immedia-semi.com/networks

**Response:**
JSON response containing information including Network ID and Account ID.

**Notes:**
Network ID is needed to issue arm/disarm calls


##SyncModules

Obtain information about the Blink Sync Modules on the given network.

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed >https://prod.immedia-semi.com/network/*network_id_from_networks_call*/syncmodules

**Response:**
JSON response containing information about the known state of the Sync module, most notably if it is online

**Notes:**
Probably not strictly needed but checking result can verify that the sync module is online and will respond to requests to arm/disarm, etc.


##Arm

Arm the given network (start recording/reporting motion events)

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login" --data-binary "" --compressed >https://prod.immedia-semi.com/network/*network_id_from_networks_call*/arm

**Response:**
JSON response containing information about the arm command request, including the command/request ID

**Notes:**
When this call returns, it does not mean the arm request is complete,  the client must gather the request ID from the response and poll for the status of the command.

##Disarm

Disarm the given network (stop recording/reporting motion events)

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --data-binary "" --compressed >https://prod.immedia-semi.com/network/*network_id_from_networks_call*/disarm

**Response:**
JSON response containing information about the disarm command request, including the command/request ID

**Notes:**
When this call returns, it does not mean the disarm request is complete,  the client must gather the request ID from the response and poll for the status of the command.


##Command Status

Get status info on the given command

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed >https://prod.immedia-semi.com/network/*network_id*/command/*command_id*

**Response:**
JSON response containing state information of the given command, most notably whether it has completed and was successful.

**Notes:**
After an arm/disarm command, the client appears to poll this URL every second or so until the response indicates the command is complete.

##Home Screen

Return information displayed on the home screen of the mobile client

**Request:**
>curl -H "Host: prod.immedia-semi.com" -H "TOKEN_AUTH: *authtoken from login*" --compressed https://prod.immedia-semi.com/homescreen

**Response:**
JSON response containing information that the mobile client displays on the home page, including:  status, armed state, links to thumbnails for each camera, etc.

**Notes:**
Not necessary to as part of issuing arm/disarm commands, but contains good summary info.


