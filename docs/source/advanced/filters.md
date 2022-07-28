# Filters

You can use filters to limit the amount of results shown in lists. Text fields support various options to control in further detail what is filtered out.

* **!...**: By placing an `!` before your text, you can search for anything that doesn't contain the text in the field.
* **...!**: By placing an `!` at the end of your text, you can search for every entity with exactly this text in the field.
* **!!**: Writing `!!` in a field will search for all entities where this field is empty.

You can combine search options on text fields by writing `;`. For example `Alex;!Smith`.

Filters and ordered columns set for an entity list are saved into your session, so as long as you stay connected you don't need to re-set them on every page.

## Attribute name

You can filter entities based on their attributes. The search fields are exact matches for both the name and value. When the value field is left empty, it looks for entities that have an attribute with that exact name. You can type `!Level` to exclude entities with an attribute called Level.

The filter doesn't evaluate attribute calculations. If an attribute has a value of `HP * Level`, searching for the result of that calculation isn't possible.

## Copy to clipboard

When filters are active, the copy to clipboard button becomes active. This copies the filters to your clipboard, and you can use those for dashboard [widget filters](/guides/dashboard#widget-filters) or for [quick link](/advanced/quick-links) filters.
