# Marketplace

The [Kanka Marketplace](https://marketplace.kanka.io) allow users to create themes, character sheets and content packs for others to use in their campaigns. Anyone can create plugins on the marketplace, but plugins can only be used in [boosted campaigns](https://kanka.io/en-US/boosters).

To see the plugins installed in your campaign, go to **WORLD** and to **Plugins**. From there you can enable, disable, update or remove plugins that are installed in the campaign.

## Introduction

Anyone can create a plugin on the marketplace. Head over to the marketplace, and if you are logged in (your login details are the same as in Kanka), click on Your Plugins in the top navigation. This interface lists all your plugins.

To create a new plugin, click on the Create a new plugin button on the top right. This brings up the new plugin interface, where you need to provide a name for your plugin, its plugin type, which allows the following:

* **Theme**: Allows you to create a theme for Kanka based on CSS.
* **Character sheet**: Allows you to create a list of attributes, and attach HTML and CSS to define how they are displayed. This means you can create custom character sheets in Kanka.
* **Content pack**: Allows you to create multiple entities (characters, locations, etc), and allow others to import these entities into their campaigns.

And lastly an optional language field, to allow people filtering on plugins based on a specific language supported by Kanka. Once you are happy with your choices (note that you can go back and edit the name and language later), click on Prepare plugin. This redirects you to the plugin overview page.

## Plugin overview page

This interface gives you access to creating and managing the versions of your plugin, and the preview images displayed on the marketplace. Versions represent the content of your plugin at various points in time. For example, you might fix a bug in your theme due to a Kanka update or user feedback, or add more entities to your content pack. Doing this is done by creating a new version.

You can access the plugin's overview page by going back to Your Plugins and clicking on a plugin's name.

## Creating a version

To create your first or new version of a plugin, click on the Create a version button. The next interface will heavily depend on the plugin type (theme, character sheet, or content pack), so we need to split the next section based on those three types.

### Fields on all plugin type versions

Every version will have the following fields, regardless of their plugin type.

* **Version name**: We recommend starting with something like "1.0" as the version name, and slowly incrementing based on future updates to your plugin.
* **Version description**: a description displayed in the marketplace and in the campaign plugins page. This is a great way to detail the changes from previous versions of your plugin.

### Theme fields

A theme will simply have a field to write your theme's CSS. This field is powered by CodeMirror for formatting.

### Character sheet fields

Create character sheets for your favourite TTRPG!

* **HTML content**: This is where you can write the HTML of your character sheet to fully cusomise the rendering of attributes, effectively allowing you to create character sheets. Some logical commands like if, else, for and more are available, and detailed here.
* **CSS content**: This is where you can write the CSS that will be included in your character sheet. We recommend prefixing your CSS classes with a code related to your plugin's name. If, for example, you're creating a character sheet for the Thirsty Lesbian Swords TTRPG, try prefixing your class names with tls-*.
* **Attributes**: This section will allow you to add attributes that get added to entities that apply this character sheet. Beware that there is a maximum of about 600 attributes per entity in the marketplace, and we won't be able to add more than supported.

At the end of the page, a preview section allows you to somewhat preview how it will look, but in practice doesn't currently work very well, due to the if/else conditions not being evaluated. Future changes to the marketplace will fix this issue.

### Content Pack fields

The most complicated plugin type. The version creation form doesn't have additional fields, but once created, in the overview page of your plugin, the version will have a new link labeled 0 entities (click to manage). Clicking this link brings up a new interface to add entities to your plugin.

## Publishing your plugin

Once you've finished creating your plugin and are happy with it, you can send the version to review. This locks it and you won't be able to make any more changes to it. Approval of plugins can take up to a few days, depending on our availability and the complexity of the plugin, but is usually done in a few hours.

In your plugin's overview page, the version will have a **Submit for review** button.

Once a version is approved, the plugin becomes available in the marketplace, and can be installed to boosted campaigns.

## Updating your plugin

With your plugin released, you realised that something isn't quite right, a spelling mistake in an entity, a wrong attribute calculation, or the CSS just isn't working as you intended. Don't worry, you don't need to start the whole process again. In the plugin's overview page, published versions will have a duplicate button, allowing you to create a new version based on the version you're duplicating. When you are happy with your changes, submit this new version for review again, and our team will review and hopefully approve it shortly thereafter.

## Installing a plugin to a campaign

Installing a plugin to a boosted campaign can be confusing at times, so this should hopefully give you a good understanding of how it works.

Once you've found a plugin on the marketplace that looks great, you need to click on the Install button on the top right of the page. This brings up an interface listing all your boosted and superboosted campaigns. Clicking on the campaign will install that plugin to your campaign.

A confirmation message will appear:

> The plugin PLUGIN-NAME was installed in the campaign CAMPAIGN-NAME.

You'll notice that the campaign name is a link. Clicking on it brings you to that campaign's plugins page, which will allow you to do the following things.

* **Theme**: If the campaign is a theme, installing it won't enable it by default. You need to go to the campaign's plugins and activate the theme.
* **Character sheet**: Adding a character sheet to the campaign will make it available in the various entities' Attributes tab in the edit page, where you can select the marketplace character sheets installed on the campaign.
* **Content pack**: If the plugin is a content pack, installing it won't automatically import all of its entities. You need to go to the campaign's plugins and click on the Sync action.

## Removing / Disabling a plugin

In the campaign's plugins page (**World > Plugins**), you can disable or remove plugins from your campaign. In the case of content packs, removing the plugin won't automatically delete entities created by the plugin.
