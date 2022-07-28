# Dice Rolls

```{admonition} Deprecated
This module is deprecated, meaning it isn't getting any new updates and will eventually be removed from Kanka. This entity type can be [enabled](features/campaigns/modules) in your campaign settings.
```

Dice rolls are a limited way to handle dice rolling for *play by post* games that don't require complicated dice rolls.

## Creating a dice roll template

Dice rolls are templates, attached from an entity, and contain a dice roll value.

Generic dice rolling is possible by writting "d20", "4d4+4", "d%" for percentile and "df" for fudge.

It is also possible to get a character's attribute by using the `{character.attribute_name}` syntax. For example, `{character.level}d6+{character.wisdom}`.

More options are available and explained on the [dice roller plugin page](https://github.com/ringmaster/dicecalc#Dice).

## Rolling a dice

To make a dice roll, view the dice roll and click on the *roll* button at the top right.

![Dice roll button](img/dice.png)
