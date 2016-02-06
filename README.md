# Mozio Backend API

# Provider

## Create

```
curl \
 --request POST \
 -d name="Fast Perú" \
 -d email=fastperu@gmail.com \
 -d phone=%2B51999888222 \
 -d language=es \
 -d currency=PEN \
 -H 'Accept: application/json; indent=4' \
 -u admin:password \
 <awsurl>/api/v1/provider/
```

## Update

```
curl \
 --request UPDATE \
 -d name="Rapidito Perú" \
 -d email=fastperu@gmail.com \
 -d phone=%2B51999888222 \
 -d language=es \
 -d currency=PEN \
 -H 'Accept: application/json; indent=4' \
 -u admin:password \
 http://<awsurl>/api/v1/provider/1/
```

## Delete

```
curl \
 --request DELETE \
 -H 'Accept: application/json; indent=4' \
 -u admin:password \
 http://<awsurl>/api/v1/provider/1/
```

## Retrieve

```
curl \
 --request GET \
 -H 'Accept: application/json; indent=4' \
 -u admin:password \
 http://<awsurl>/api/v1/provider/2/
```

# Service Area

## Create

* http://geojson.io/#map=12/-12.0397/-77.0526
  * We can create a polygon here and copy only the "geometry"
    dictionary from the GeoJSON created there and paste it in a
    file. Then call CURL with `--data-urlencode polygon=@polygon.json`

```
curl \
 --request POST \
 -d name="Lima Downtown" \
 -d provider=5 \
 -d price=9.33 \
 -d polygon='{"coordinates": [[[-77.06153868556186, -12.018501931478212], [-77.008666981468, -12.003054814405393], [-76.9297027480803, -12.04402131242793], [-77.01278685451477, -12.081960118041692], [-77.080078114271, -12.061816287965616], [-77.07458495020923, -12.036634372364633], [-77.06153868556186, -12.018501931478212]]], "type": "Polygon"}'  \
 -H 'Accept: application/json; indent=4'  \
 -u admin:password  http://<awsurl>/api/v1/servicearea/
```

## Update

```
curl \
 --request POST \
 -d name="Lima Downtown" \
 -d provider=5 \
 -d price=15.33 \
 -d polygon='{"coordinates": [[[-77.06153868556186, -12.018501931478212], [-77.008666981468, -12.003054814405393], [-76.9297027480803, -12.04402131242793], [-77.01278685451477, -12.081960118041692], [-77.080078114271, -12.061816287965616], [-77.07458495020923, -12.036634372364633], [-77.06153868556186, -12.018501931478212]]], "type": "Polygon"}'  \
 -H 'Accept: application/json; indent=4'  \
 -u admin:password  http://<awsurl>/api/v1/servicearea/1/
```

## Delete

```
curl \
 --request DELETE \
 -H 'Accept: application/json; indent=4'  \
 -u admin:password  http://<awsurl>/api/v1/servicearea/1/
```

## Retrieve

```
curl \
 --request GET \
 -H 'Accept: application/json; indent=4'  \
 -u admin:password  http://<awsurl>/api/v1/servicearea/1/
```


# Consult which ServiceAreas are on the desired point

```
curl \
 --request GET \
 -H 'Accept: application/json; indent=4' \
 -u admin:password http://<awsurl>/api/v1/point/-12.0589/-77.0559/
```
