# Permissions

Permissions in Kanka are a complex subject, with several permissions systems all working in tandem. The first element of permissions is on the campaign itself, followed by entities, and lastly by elements attached to an entity.

## Campaign Permissions

Campaign permissions are controlled on a role basis. This means each role in your campaign has varying permissions, and members in those role automatically inherit permissions from their roles.

By default, each campaign is created with an Admin role, a Players role, and a Public role. To manage your campaign's roles and their permissions, in the sidebar click on World, then on Roles in the submenu. From there, clicking on a role's name will bring you to it's permission screen.

### The Admin Role

The Admin role is for everyone with full control on the campaign, able to see and interact with just about everything. This includes changing the campaign, adding or removing members, creating, updating or deleting any entity, and most dangerously deleting the campaign.

When creating or editing an entity, the last field is the privacy field. Is that field is checked, the entity will only be visible to members of the campaign's admin role.

You cannot directly add members to your campaign's admin role. You first have to invite them to your campaign into another role, and once they have joined, you can add them to the admin role.

This role cannot be deleted from the campaign.

### The Player Role

This role is created by default as a catch-all role for all the people you invite to the campaign. By default, it has no permissions, meaning that inviting a member to your campaign will result in them seeing the campaign, but not seeing anything in it.

You can give general permissions to the role to view all characters.

If for example your player role has the permissions to create characters but not update them, players who create a character will automatically get the permission to update and delete the created character.

This role can be deleted.

### The Public Role

The public role comes into play when your campaign is public, meaning non-members of the campaign can view its content. The same way a player inherits their permissions from the player role described above, a user visiting your campaign without being a member or logged in will have the public role's permissions.

You can only control the "viewing" permission on this role. And as with the admin role, this role cannot be deleted.

## Entity Permissions

Having role permissions is usually enough for most scenarios, but sometimes you'll want to allow a specific user to update a location, or allow another to add posts on a specific quest. This can be done on the entity.

### Setting entity permissions

When creating or editing an entity, a Permissions tab is displayed towards the end. This allows you to allow or deny specific actions for the roles and members of your campaign.

###  Role permissions

By default, the role actions will show a small green checkmark if that role can already perform that action.

The campaign's admin role isn't displayed, as it has access to everything.

### User permissions

The same way role permissions show a green checkmark if the role can perform an action, the same is true for a user. This evaluates all the roles of each user to figure out what they can do.

Members of the campaign's admin role don't appear in this list, since they have access to everything.

### Permissions tab not available

If a campaign has too many members (10 or more), the permission tab on the create or edit entity interface isn't available, due to the processing power required of calculating each user's permissions on the fly. You can still access the permission interface on its own after having created the entity. To do so, view the entity, and in the entity's left side menu, click on Permissions.

## Element permissions


Elements attached to entities have another permission concept. Instead of a complex setup, they have a Visibility dropdown.

Here is a quick run down of what each of the permissions do.

* **Admin**: Only available to members of the campaign's admin role, this makes the element only visible to other admins.
* **Self**: Only available when creating an element, this makes the element only available to you. This means you can hide information from admins. Elements with this visibility don't show up when impersonating a user.
* **Self + Admin**: This element is only available to you and members of the campaign's admin role. For example, if you as a player want to share something with the admin, but not the other players.
* **Members**: Comes into play if the campaign is public. This element will only be available to all members of your campaign, and not the public role.
* **All**: This element is visible to all. 


## Next up

> [Testing permissions](../guides/testing-permissions)