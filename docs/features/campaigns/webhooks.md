# Webhook

Webhooks are a feature for [premium campaigns](https://kanka.io/premium) introduced with Kanka version 2.4.

## Access

To access the campaign's webhooks interface, go to **Settings > Webhooks**. This interface, only available to members of the campaign's admin role, allow them to define, toggle, and test webhooks.

## Triggers

Webhooks can be defined to trigger on entity creation, update, or deletion. Webhooks can be set to only trigger when entities with specific tags are affected.

## Types of webhooks

Webhooks are split into two types

* **message** sends a custom message to a URL.
* **payload** sends a json payload to a URL.

### Payload

The payload is a json object with the following structure:

```json
{
    "event": {
        "id": "21321445435345346",
        "type": "Payload",
        "webhook_id": 42,
        "timestamp": "2023-08-22 20:25:07",
    },
    "entity": {
        "data": [
                    {
                        "id": 1,
                        "name": "Thaelia",
                        "entry": "\n<p>Lorem Ipsum.</p>\n",
                        "image": "{path}",
                        "image_full": "{url}",
                        "image_thumb": "{url}",
                        "has_custom_image": false,
                        "is_private": true,
                        "location_id": null,
                        "entity_id": 5,
                        "tags": [],
                        "created_at":  "2019-01-30T00:01:44.000000Z",
                        "created_by": 1,
                        "updated_at":  "2019-08-29T13:48:54.000000Z",
                        "updated_by": 1,
                        "location_id": 4,
                        "type": "Kingdom"
                    }
            ]
    }
}
```
## Mappings

Message webhooks have the added functionality of mappings that can be used to display variable data, like name of the entity, the url of said entity or the name of the user who updated it, these can be included in the custom message using `{name}` for the name of the entity, `{url}` for the url of the entity and `{who}` for the name of the user who performed the action.

For example, a custom message for an entity updated webhook could look like: `User {who} has updated {name} accesable in {url}.`.

## Testing a webhook

In the list of webhooks, it is possible to test a specific one. This will send data to the url with some fake data regarding the entity.
