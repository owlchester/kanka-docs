# Campaign Theming

The first half of the following Youtube videos describes this article.

[![Customising your Kanka campaign](https://img.youtube.com/vi/ynX5jimy8Lo/0.jpg)](https://youtu.be/ynX5jimy8Lo)

[Boosted campaigns](https://kanka.io/en-US/boosters) can write custom CSS for their campaigns. This interface is access in **World** and **Theming**.

To keep what little sanity you have left, it is recommended to split up your css into multiple themes.

## Fonts

CSS fonts are only properly imported when they are at the beginning of the CSS file. Since all the campaign's active themes are merged together in the order defined by the campaign's admins, it is recommended to have a `_fonts` theme in first position for all of your font import rules.

### Marketplace

Some older [marketplace](marketplace/marketplace) plugins will require you to add font rules to your Kanka campaign. Having a `_fonts` theme at the top makes this super easy. Since October 2022, marketplace themes no longer need this workaround.
