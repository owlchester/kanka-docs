# Visibility

Many elements in Kanka have a visibility option, allowing for a control on who sees what without having to set up complex permissions.

Here is a list of what each visibility does.

* **All**: Everyone can see this element.
* **Admin**: Only members of the campaign's admin role will see this element.
* **Self**: Only the user who created the element will see it.
* **Self & Admin**: A combination of the Admin and Self visibilities.
* **Members**: Only members of the campaign will see the element. Useful for a public campaign where members of it should see more than a public viewer.

In addition to the element's visibility value, if it is linked to an entity, the entity's permission will also come into play. For example, if a relation is visible to all, but the relation's target is only visible to admins, then only admins will see the relation.
