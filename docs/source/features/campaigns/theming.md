# Campaign Theming

The first half of the following Youtube videos describes this article.

[![Customising your Kanka campaign](https://img.youtube.com/vi/ynX5jimy8Lo/0.jpg)](https://youtu.be/ynX5jimy8Lo)

Administrators of [premium campaigns](https://kanka.io/premium) can write custom CSS for their campaigns. This interface is accessed in `Settings > Theming`.

To keep what little sanity you have left, it is recommended to split up your CSS into multiple themes.

## Theme builder

When creating your first campaign style, you'll be asked if you want to use the [theme builder](/features/campaigns/theme-builder) instead. The theme builder is a great way of changing just the various colours of Kanka without having to learn CSS!

## Fonts

CSS fonts are only properly imported when they are at the beginning of the CSS file. Since all the campaign's active themes are merged together in the order defined by the campaign's admins, it is recommended to have a `fonts` theme in first position for all of your font import rules.

[![Adding custom fonts](https://img.youtube.com/vi/pzQN4sqDBMs/0.jpg)](https://youtu.be/pzQN4sqDBMs)

### Marketplace

Some older [Marketplace](marketplace/marketplace) plugins will require you to add font rules to your Kanka campaign. Having a `_fonts` theme at the top makes this super easy. Since October 2022, Marketplace themes no longer need this workaround.

## Deep dive

Our amazing Salvatos has written extensively on how to customise Kanka using CSS. You can find his [introduction to campaign CSS here](https://salvatos.gitbook.io/kanka-cookbook/css/introduction-to-campaign-css).

## Tutorials

We have a few [tutorials on our blog](https://blog.kanka.io/category/tutorials/), but the best place to get help is on our [Discord](https://kanka.io/go/discord).