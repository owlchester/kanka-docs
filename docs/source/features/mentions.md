# Mentions

[![Mentions](https://img.youtube.com/vi/GLVI3XV5PO0/0.jpg)](https://youtu.be/GLVI3XV5PO0)

In the entry field of entities and posts, you can type `@` followed by 3 characters to search for an entity of the world.

## Filtering

Filtering for the exact entity you are looking for is easy.

Type `@Entity_Name` to find an entity with a space in the name.

Type `@=Entityname` to find an entity that has exactly that name.


## Advanced mentions

Link to other entities by typing `[` and the first few characters of an entity to search for it. This will inject `[entity:123]` in the text editor. To customise the name of the entity displayed, you can type `[entity:123|Alex]`. To set the entity's subpage, use `[entity:123|page:inventory]`. Some options are inventory, attributes, abilities, assets, relations, profile.

The advanced mention can also specify the HTML anchor the link should point to using `[entity:123|anchor:post-69]`.

You can also display a field from the entity instead of its name in the link with `[entity:123|field:location]`. Some options are type, location, race, gender, pronouns, title. You can even inject the target's entry with `[entity:123|field:entry]`.

```{admonition} Limitation
While you can render a target's entry with `[entity:123|field:entry]`, the target's entry won't include parsed mentions. This is to avoid performance issues and crashing the servers with loops. 
```

Parameters can also be passed along to the entity link. For example, specify which year and month get shown on a calendar with `[calendar:100|params:year=2022&month=07]`. The same can be done with ordering sublists. For example, order family subfamilies by location name with `[family:100|page:families|params:k=location.name&o=asc]`.

## Attributes

Referencing attributes of this entity is also possible. Simply type `{` and three letters or more to display matching attributes on the entity. This injects `{attribute:123}`, 123 being the attribute's unique number in Kanka. You can copy-paste this reference in other entities to reference attributes from other entities.

## Calendar months

Type `#` to get a list of months from your calendars.

## Formatting

The list of allowed HTML tags and attributes can be seen on our [Github](https://github.com/owlchester/kanka/blob/develop/config/purify.php).
