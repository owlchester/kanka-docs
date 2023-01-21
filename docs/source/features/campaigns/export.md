# Export

Campaigns can be exported once a day. To start exporting a campaign, go to **World** and **Export**.

Once the process has been started, one of the Kanka severs will try to generate two files.

The first one is the **campaign export**. This is a zip with every single entity sorted by type and exported in `JSON` format. This export should never fail.

The second one is the **campaign assets**. This is a zip with all the images of your entities. However, if the total size of the campaign's images is over 128MB, this export fails. The first export still includes the path to download each entity's image individually.

## Who can export the data?

Only members of the campaign's **admin** role can initiate and download the campaign export. Once the files are ready, all members of the campaign's admin role will get a notification.

## How long is the download available?

The ZIP files are downloadable for 30 minutes after they've been generated, before being deleted from our servers.

## How to import the export data?

It is not possible to import an export into Kanka. Exports are meant for your own peace of mind, or to backup your data before leaving Kanka. Kanka automatically performs two complete backups of all your data twice a day.