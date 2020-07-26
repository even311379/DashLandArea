# DashLandArea

A dash app to calculate land area

---
## Purpose

How come there is no a feasible area calculation app for my country. How could this happen? 
There is actually some area calculation app but the units is just not feasible for out daily usage.
The language support is also lacking.

So... why don't I create one?


---
### about dash-dl

Dash-dl is a third-party library that incorporate leaflet map for 
the interactive styles of dash framework. Which makes it super easy to to receive input and
 create output based on the map. However, this library is not well documented yet for pure
  python users like me. 

Any way... here is my notes:

(1) changing default map is achieved from set url in dl.TileLayer

ex: 
```
dl.TileLayer(url='http://mt0.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', maxZoom=20)
```
The url can be found on  https://leaflet-extras.github.io/leaflet-providers/preview/ or just google 'leaflet tile url'.
The point here is that the answer you found is something like this:
```
googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
});
```
you have to replace '{s}' to one of the subdomains as my example above. And hopefully, you can get the desired map layer. 