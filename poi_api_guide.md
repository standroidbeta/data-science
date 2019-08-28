## Places of Interest API

**POST Request** eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/

Body for HTTP request:
~~~json
{
	"latitude": 35.7796, 
	"longitude": -78.6382,
	"distance": 5
}
~~~
Example JSON response: <br>
![](Pictures/post_request.png)

### API Routes
| Route                | URL                                                                  |
| -------------------- | :------------------------------------------------------------------: |
| Walmart Data         | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_walmart         |
| Rest Area Data       | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_rest_area       |
| Weigh Station Data   | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_weigh_station   |
| Road Descent Data    | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_road_descents   |
| Tourist Site Data    | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_tourist_sites   |
| Campsite Data        | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_campsite        |
| Dump Station Data    | eb-flask-rv-dev.us-east-1.elasticbeanstalk.com/fetch_dump_station    |
