# Map Markers

Markers turn a map into a browsable part of your world. A marker can identify a place, add a label or shape, and link readers to an entry.

Create and edit markers directly in [Map Explorer](explore.md). The old **Markers** tab remains available for managing existing records, but it is no longer the place to add markers.

## Types of markers

Map Explorer has five marker types. Choose a type from the toolbar at the bottom of the map, then draw or place it on the canvas.

### Pin

The standard point marker: click the map to place it. Choose one of the built-in icons, or use a custom icon in a premium campaign.

#### Custom Icon

Premium campaigns have access to **custom icons**, which can be icons from Font Awesome or RPG Awesome.

For Font Awesome, copy the icon's code snippet (for example, `<i class="fa-solid fa-user"></i>`) into the custom icon field. Kanka converts it to its class value, such as `fa-solid fa-user`.

For RPG Awesome, enter the icon name prefixed by `ra `; for example, `ra ra-aura`.

You can also paste a custom SVG from a vector drawing app.

_SVGs are resized to fit the pin, so use a viewbox that uses the available width and height._

#### Draggable

Enable **Draggable** in the marker's advanced options to let editors move the pin directly on Map Explorer. Its new position is saved automatically.

### Text

A text label displays a marker's name on the map. Use it for a kingdom name, region, or other annotation. Like a pin, it can be repositioned by editors.

### Circle

Click and drag to draw a circle. You can later resize or move it directly on the map.

### Area

An **area** is a closed, custom shape. Click to add points and double-click to close it. When editing an area, drag its points or edges to reshape it.

Use the marker colour for its fill, then set its border colour, border width, and opacity in the details panel. Areas replace the former **polygon** marker type.

### Path

A **path** is an open line made of points. Use it for roads, rivers, routes, walls, or borders. Click to add points and double-click to finish the path; drag its points or edges later to update its course. Set its colour, line width, and opacity in the details panel.

## Overall fields

All marker types share these fields.

* **Name** or **linked entry**: provide at least one. If both are set, the name is used on the map and in the details panel.
* **Group**: assign the marker to a [map group](groups.md), or leave it ungrouped.
* **Colour** and **Opacity**: control the marker's appearance. Areas also have a border colour and width; paths have a line width.
* **Visibility**: controls who can view the marker.
* **Description**: write a custom entry shown when someone selects the marker. It can include links, mentions, and gallery images.
* **Advanced**: set a CSS class or enable dragging where that marker type supports it.

When a marker is selected, Map Explorer shows its custom description and, if linked, a preview of the entry.
