# Mozio Group
### _JSON REST API_

Python coding test. 

## Use with method Get: List all providers
```sh
https://moziogroup.herokuapp.com/api/v1/providers
```
Returns for example:
```json
{
    "id": 1,
    "name": "Fedex",
    "email": "admin@fedex.com",
    "phone_number": "423522312",
    "language": "ENG",
    "currency": "USD"
}
```

## Use with method Post: Create a new provider
```sh
https://moziogroup.herokuapp.com/api/v1/provider/new
```
For example:
```json
{
    "name": "Fedex",
    "email": "admin@fedex.com",
    "phone_number": "423522312",
    "language": "ENG",
    "currency": "USD"
}
```
## Use with method Get, Put, Delete: Recover, Update and Delete an existing provider
At the end it has the provider id, for example 1
```sh
https://moziogroup.herokuapp.com/api/v1/provider/1
```

## Use with method Post: Create a new zone (polygon)
```sh
https://moziogroup.herokuapp.com/api/v1/zone/new
```
For example:
```json
{
    "name": "Zone 1",
    "price": "150.00",
    "polygon": "[0,0], [10,10], [0,10], [10,0]",
    "provider": 1
}
```

## Use with method Get, Put, Delete: Recover, Update and Delete an existing zone
At the end it has the polygon or zone id, for example 1
```sh
https://moziogroup.herokuapp.com/api/v1/zone/1
```

## Use with method Get: Find a provider in the area, sorting by price, id_provider and name
It should take a lat/lng pair as arguments and return a list of all polygons that include the given lat/lng. For example lat=5 and lng=5
```sh
https://moziogroup.herokuapp.com/api/v1/zone/?lat=5&lng=5
```



