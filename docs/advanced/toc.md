# Table of contents

The text editor has an option to inject a *table of contents* into the description field. This will inject a `{table-of-contents}` script into the description field.

The table of content is only rendering when viewing an entry. This will replace the `{table-of-contents}` with a table of contents based on the entry's `h1` to `h6` headings.

Note that this feature is limited to the current context. For example, you can't have this script in a note's description field, and expect it to create a TOC based on [articles](/features/articles) on the note.