
## Transforming an entity's type

Since entities all share a similar base, this means you can change an entity's type after you've created it. Say you create an [event](entities/events), fill it out, and later realise you want an [item](entities/items) instead. No worries, you can change the entity's type in its **actions**, accessed by clicking on the "cog" next to the entity's name.

![Transforming an entity](img/transform.png)

## Data gained, data lost

This transform will keep all the shared data the two entity types. For example, if you transform an event to an item, the item has no _date_ field, so that is lost. Transforming the item back to an event will not recover the _date_ value.

However, the name, type, entry, tags, permissions, attributes, posts, reminders, relations etc are all kept. You also don't need to update any **mentions** targeting the original event, Kanka automatically keeps track and updates all of them!