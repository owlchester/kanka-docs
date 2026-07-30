# Map Explore

A map's **explore** page, Map Explorer, is the main way to view and work with a map. It shows the map and its markers in a full-screen canvas.

Use the list button at the top left to open the **legend**. The legend lists groups and ungrouped markers, can be searched, and lets you select a marker without finding it on the map.

Selecting a marker opens its details panel. The panel can show its custom description, linked entry, group, and—where configured—the distance of a path or area. Editors can also center the map on the marker, duplicate it, edit it, or delete it from this panel.

## Create and edit markers

If you can edit the map, use the toolbar at the bottom of Map Explorer. There is no separate edit mode and no need to use the old **Markers** tab to add markers.

* **Pin**: click the map to place a pin.
* **Text**: click the map to place a text label.
* **Area**: click to add each point, then double-click to close the area.
* **Circle**: click and drag to draw a circle.
* **Path**: click to add points along a route, then double-click to finish it.

After drawing or placing a marker, complete its details in the side panel and save it. The **Details** button reveals its colour, icon, group, description, opacity, visibility, and advanced options. Areas and paths can also have a border width; areas can have a separate border colour.

To change an existing marker, select it and choose **Edit details**. Pins, labels, and circles can be moved directly on the map; areas and paths expose draggable points and edges for reshaping. Press <kbd>Escape</kbd> to cancel the current drawing or edit operation.

### Rapid creation

Turn on **Rapid** in the toolbar when placing several markers of the same type. After you save a marker, the selected drawing tool stays active so you can immediately place the next one.

## Map settings

Editors can open **Map settings** from the map name menu at the top left. These settings apply immediately to the map:

* grid size
* minimum, maximum, and initial zoom
* distance unit label and measurement scale
* the initial center, either by selecting a point on the map or a marker
* the legacy pin-style switch

The regular map edit page still contains these settings too, as well as settings that are not part of Map Explorer, such as OpenStreetMap and marker clustering. See [Map Setup](setup.md) for the full breakdown.

## Measurement tool

Set both a **Distance Unit label** and **Distance measurement** in Map settings to enable the ruler. The ruler button appears at the lower left of the map.

Click it, then click on the map to add waypoints and see the distance between them.

### Usage

* Press <kbd>Escape</kbd> to finish the current measurement. Press it again before placing a point to turn off the ruler.
* Double-click also finishes the measurement and turns off the ruler.

## Dashboard widget

A map can be pinned to a dashboard. To do so, add an **entry preview** widget linked to the map to the dashboard. Markers can be clicked on the dashboard, which will open the target entry.
