# Property Kits

**Property kits** are a complicated beast. When using [properties](/features/properties) on your [locations](/entries/locations), you might be re-creating the same properties over an over. You could create a [location archetypes](/guides/archetypes), or use [property kits](/entries/property-kits).

While this video uses a very old interface, the concepts still hold true to this day.

[![Property kits](https://img.youtube.com/vi/qKnTpuePqUA/0.jpg)](https://youtu.be/qKnTpuePqUA)

## Setting up a property kit

Say you're constantly adding the following properties to your cities.

* **Population**
* **Wealth**
* **Crime**

Doing so each time you're adding a city is tedious, so let's make this process a lot easier, especially as you end up tracking more properties.

In your campaign sidebar, click on **Property kits** at the bottom of it, and on the **+ Property Kit** button at the top right to create a new property kit.

![New property kit button](img/property-kits.png)

### Fields

Property kits have the following fields.

* **Name**: The name of the new entry, in our example, let's call this one **City**.
* **Parent property kit**: For your own organisation, you can nest property kits. If you end up with multiple templates focused on locations and multiple on characters, you might create a parent property kit for that.
* **Category**: If kit, newly created entries of that category will automatically have the properties of this template added to them. For example, if all of your Journals have a "levelled up" property, you can automate this process for new journals. In our example, let's leave this field empty.

Next up, fill out the **Properties** tab with our 3 example properties from above. Save the property kit and head on to the next step.

## Applying a property kit

With the property kit created, it's time to test it out. Go to your campaign's [locations](/features/entries/locations), and create a start creating a new one.

In the new location's **Properties** tab, click on the **Property Kit** option to list your campaign's property kits. This list also includes [character sheets](/plugins/character-sheets) from the [plugins library](/plugins/plugins). Select our example **City** property kit.

This does not add the new properties _yet_, as property kits are only applied when the entry is being saved. Save your new location, and you should see it's properties going to the new location's properties subpage.

## Resyncing properties from a property kit

When you add a new or change and existing property to a template, it does not automatically change on all entries that have the property kit applied. You need to manually re-apply the kit. Luckily, you can do this with the [bulk](/advanced/bulk) features.

## Nested kits

We previously left the [parent](/features/nested) field empty. However, this can be incredibly useful to organise your property kits.

Let's say you have a property kit called **City**, which has some properties, and itself has two other property kits. When you apply **City** to an entry, it will add properties from **City** and the children property kits.

## Category

Setting the **category** field will automatically apply the property kit to new entries. Note that this only works when creating an description with the form. This does not work with the [quick creator](/features/quick-creator) or [new mentions](/features/mentions#new-entity).