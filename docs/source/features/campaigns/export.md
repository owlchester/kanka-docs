# Export

Campaigns can be exported once a day. To start exporting a campaign, go to **World** and **Export**.

Once the process has been started, one of the Kanka severs will try to generate two files.

The first one is the **campaign export**. This is a zip with every single entity sorted by type and exported in `JSON` format. This export should never fail.

The second one is the **campaign assets**. This is a zip with all the images of your entities. However, if the total size of the campaign's images is over 128MB, this export fails. The first export still includes the path to download each entity's image individually.

## Import

It is not possible to import an export into Kanka.