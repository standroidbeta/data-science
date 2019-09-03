## Places of Interest API

This API returns the coordinates and general information of a user's desired place of interest relative to the user's current location and desired radius. 

### API Routes
| Route                | URL                                                                  | Type |
| -------------------- | -------------------------------------------------------------------- | ---- |
| Walmart Data         | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_walmart         | Post |
| Rest Area Data       | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_rest_area       | Post |
| Weigh Station Data   | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_weigh_station   | Post |
| Road Descent Data    | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_road_descents   | Post |
| Tourist Site Data    | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_tourist_sites   | Post |
| Campsite Data        | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_campsite        | Post |
| Dump Station Data    | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_dump_station    | Post |

### HTTP Request
Example Body for HTTP request:
~~~json
{
	"latitude": 35.7796, 
	"longitude": -78.6382,
	"distance": 5
}
~~~
### HTTP Response
Example JSON response (Walmart Data): <br>
![](Pictures/post_request.png)

