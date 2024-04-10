# Webhook

Webhooks are a feature for [premium campaigns](https://kanka.io/premium) introduced with Kanka version 2.4.

## Access

To access the campaign's webhooks interface, go to **Settings > Webhooks**. This interface, only available to members of the campaign's admin role, allow them to define, toggle, and test webhooks.

## Triggers

Webhooks can be defined to trigger on entity creation, update, or deletion. Webhooks can be set to only trigger when entities with specific tags are affected.

## Types of webhooks

Webhooks are split into two types

* **message** sends a custom  message to a URL.
* **payload** sends a json payload to a URL.

### Payload

The payload is a json object like the following

```json
{
    "event": {},
    "entity": {}
}
```

## Testing a webhook

In the list of webhooks, it is possible to test a specific one. This will send data to the url with some fake data regarding the entity.