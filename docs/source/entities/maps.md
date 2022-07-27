# Maps

Who doesn't love a big map full or markers? This module is more useful for representing your world, rather than a battle map with live updates for your players to see.

## Map fields

Let's have a look at fields that are unique to maps.

* **Parent Map**: If this level 3 of a bigger dungeon that also is a map? If so, use the parent map to "place" this map inside another.
* **Location**: Useful if this map is the map of a kingdom, town, dungeon, etc. Link the location, and the map will be available in the location's profile sidebar.
* **Image**: This is the main image, which will serve as the map image, and also the thumbnail image of the map in lists.

### Settings

In the settings tab, you'll find the following fields.

* **Use OpenStreetMaps**: If you want to use a map from the real world instead of a custom image, check this option. You still need an image for the map, but it will only be used as a thumbnail.
* **Cluster markers**: After adding several markers on your map, it will quickly become messy and unreadable. This option clusters markers that are close together until you zoom in enough.

#### Zoom levels

This fields control the zoom (aka when scrolling on a map) levels.

#### Centering

By default, a map loads at coordinates 0,0. You can change this by providing new coordinates, or having your map center on a specific marker.

### Layers

When editing a map, you can add layers to it. These are images that are super-imposed on the map, and can be toggled on/off from anyone viewing the map. Useful to upload an image of a dungeon with the traps, only visible to the campaign's admins.

### Groups

When editing a map, you can add groups to this. This allows you to group markers together, and show/hide all markers of a group at the click of a button. For example all your settlements, rivers, or mountain markers.

### Markers

When editing a map, this is where you'll click to add markers to the map.

These have a lot of fields.

* **Name** vs **Entity**: At least one of these has to be filled out. If both are filled out, the **name** will be used when hovering/viewing the marker.

#### Markers

The basic marker on maps, think of it like a "pin" on a map.

#### Label

A block of text on the map. This can't be moved around easily, but offers a clear visual different from markers. For example a kingdom's name.

#### Circle

Draw a tiny or huge circle on the map. Go crazy!

#### Polygon

The most complicated marker, this option is to draw custom shapes on the map. For best results, create a polygon with `0,0 100,0 0,100` and save it. Once saved, edit the marker to enable clicking on the map to add coordinates. It's a messy process, but allows fully custom shapes.

The stroke fields are to control the polygon's visuals (border, background color, opacity).

## Explore

A map's **explore** page is the best way to consume its data. This shows the map, the layers, groups, and markers. Clicking on a marker will load its data in the sidebar. This is used from the marker's custom entry field, and from the marker's linked entity.

## Dashboard widget

TBW