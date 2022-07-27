# Table of contents

The text editor has an option to inject a *table of contents* into the entry field. This will inject a `{table-of-contents}` script into the entry field.

The table of content is only rendering when viewing an entity. This will replace the `{table-of-contents}` with a table of contents based on the entry's `h1` to `h6` headings.

Note that this feature is limited to the current context. For example, you can't have this script in a note's entry field, and expect it to create a TOC based on [posts](features/posts) on the note.