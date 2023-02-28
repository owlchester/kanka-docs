# Visibility

Many elements in Kanka have a visibility option, allowing for a control on who sees what without having to set up complex permissions.

Here is a list of what each visibility does.

* **All**: Everyone can see this element.
* **Admins**: Only members of the campaign's admin role will see this element.
* **Only me**: Only the user who created the element will see it. This can be useful if a campaign has several admins and there is a need for secrets between the admins.
* **Only me & Admins**: A combination of the Admin and Only Me visibilities.
* **Members of the campaign**: Only members of the campaign will see the element. Useful for a public campaign where members of it should see more than a public viewer.

## Permission chaining

In addition to the element's visibility value, if it is linked to an entity, the entity's permission will also come into play. We call this **permission chaining**. For example, if a relation is visible to all, but the relation's target is only visible to admins, then only admins will see the relation.

This permission chaining between an element and an entity works for the following elements:

* Character organisation
* Inventory
* Map marker
* Quest element
* Relation
* Reminder
* Timeline Element