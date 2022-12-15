# Calendars

The most complicated and complex feature of Kanka, calendars are a frequent source of headaches for the Kanka team.

At a fundamental level, calendars are used to track day-by-day events of your world. Calendars and entities are linked through [reminders](/features/reminders).

## Long-lasting reminders

Reminders are only displayed over the span of maximum 2 months. If your reminder lasts longer (for example a multi-year war), create multiple reminders. For example:

* **War declaration**: date the war started
* **First battle**: date of the first battle
* **Paris falls**: date when a city fell
* **Peace deal**: date the war ended

## Gregorian calendar

If you want to mimic the gregorian calendar (the one used in most of the western world), you can copy [this calendar](https://kanka.io/en/campaign/1/calendars/2065) to your campaign. Note that it isn't an exact copy of the gregorian calendar, as popes and kings over the centuries have added/removed days or even months from it willy-nilly.

## Advancing calendars

If you want your calendar to increment by one day automatically every day, you can do so in the calendar's **Advancing date** option in the **Calendar** tab. This advances the day by one every night at `00:00UTC`.

## Parent Calendars

A calendar can have a [parent](/features/nested) calendar. This is practical if you are running several campaigns and want multiple "today"s.

Once you have your base calendar, create a copy of it, to duplicate the config of days, weeks, months, moons, seasons, etc, and set the  template **parent calendar** field to the parent.

When viewing the child calendar, it will show all of its reminders, **as well as the reminders from the parent**.

```{info} Warning
Reminders form a parent calendar cannot be hidden or removed from a child. Doing so will delete the reminder from the parent, rather than hide it in the child. Reminders from the parent calendar aren't duplicated but simply shown.
```

## Eras

If you want to split your calendar into multiple eras, create multiple calendars and use the **Suffix** field. This tremendously reduces the strain on the Kanka servers.

## Min and Max year

The calendar's year can be -2'000'000'000 to 2'000'000'000. The same is true for reminders. This means you can have a calendar and reminders **before** your calendar's year zero.

## Year Zero

By default all calendars start on year zero, if you want, you can disable this when creating a new calendar, making it start on year 1.

## Calendar widget

A calendar can be displayed on the dashboard. [Find out more](/guides/dashboard#calendar).


## Why doesn't the calendar support X, Y or Z feature?

The calendar is by far the most complex feature of Kanka, and the one most prone to breaking when something changes. Adding a single new feature to it can result in weeks of work, with even more weeks of bug fixing afterwards. This is why it is often memed on in the [Discord](https://kanka.io/go/discord).

Other tools like fantasy-calendars have a team working solely on their calendar app for years, which result in more features by virtue of not having to build a whole worldbuilding and TTRPG management tool at the same time.
