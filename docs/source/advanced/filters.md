# Filters

As your campaign becomes larger and content no longer fits on a single page, for example for the world's characters, filters become an essential tool for finding the info you are searching for.

Every main list of entities accessibly from the [sidebar](/features/campaigns/sidebar) can be filtered. To open the filters, click on the **Filters** box above the list of entities.

![Open the filters](img/filters-box.png)

This opens up tons of filter options.

```{admonition} Additive filters
Filters are aditive, which means that when providing a `type` and a `location` filter, only entities that match both criteria are displayed.
```

## Text matching

Text fields support various options to control in further detail what is filtered out.

* **!...**: By placing an `!` before your text, you can search for anything that doesn't contain the text in the field.
* **...!**: By placing an `!` at the end of your text, you can search for every entity with exactly this text in the field.
* **!!**: Writing `!!` in a field will search for all entities where this field is empty.

You can combine search options on text fields by writing `;`. For example `Alex;!Smith`.

Filters and ordered columns set for an entity list are saved into your session, so as long as you stay connected you don't need to re-set them on every page.

## Location name

You can filter entities based on their location. The search field looks for entities that have a location with that exact name. You can use the selection box at the right of the field to select between 4 different behaviours for the filter, these are: include, which includes all entities in that location; exclude, which excludes all entities in that location; with children, which includes all entities in that location or any of all its children locations, and none, which shows all entities without a defined location.

## Attribute name

You can filter entities based on their attributes. The search fields are exact matches for both the name and value. When the value field is left empty, it looks for entities that have an attribute with that exact name. You can type `!Level` to exclude entities with an attribute called Level.

The filter doesn't evaluate attribute calculations. If an attribute has a value of `{HP} * {Level}`, searching for the result of that calculation isn't possible.

## Copy filters to clipboard

After filling out the filters and clicking the **Filter** button, the list of entities will be updated. At this point, in the filters box, the **Copy filters to clipboard** button becomes active. Clicking it copies the filters to the clipboard, which can be pasted in the dashboard [widget filters](/guides/dashboard#widget-filters) and [quick link](/advanced/quick-links) **filters** fields.

![Copy filters to the clipboard](img/filters-copy.png)


