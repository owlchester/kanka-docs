# Rich Text Editor

```{admonition} Warning
This document talks about the Experimental text editor in Kanka. You can switch to it in your [appearance settings](https://app.kanka.io/settings/appearance). This editor is built on top of the TipTap editor.
```

The rich text editor helps you format text, add links and images, reference entries, create tables, and edit HTML.

Most formatting tools appear when you select text or another item in the editor.

## Format Text

Select some text to open the formatting menu. You can:

- Change the text to a paragraph or heading
- Use headings from level 1 to level 5
- Make text bold
- Make text italic
- Add a strikethrough
- Underline text
- Change the text colour
- Add a background highlight colour
- Add or edit a link
- Turn the text into a quote
- Align text to the left, centre, or right
- Create a bullet list
- Create a numbered list
- Remove formatting

The colour menus include preset colours and remember your recently used colours. You can also enter a custom colour in the `#RRGGBB` format.

## Slash Commands

Type `/` to open the command menu. Continue typing to search for a command.

Use the arrow keys to select a command, then press `Enter`. Press `Escape` to close the menu.

Available commands include:

| Command | Result |
|---|---|
| Source | Edit the HTML source |
| Gallery | Insert an image from the gallery |
| Insert Media | Upload an image from your device |
| Table | Insert a table |
| Heading 1 | Create a large heading |
| Heading 2 | Create a medium heading |
| Heading 3 | Create a small heading |
| Bullet List | Create a bullet list |
| Numbered List | Create a numbered list |
| Task List | Create a checklist |
| Quote | Create a quote block |
| Code Block | Create a code block |
| Horizontal Rule | Insert a divider |

Some commands, such as gallery and media upload, may only be available when the page supports them.

## Reference Entries

Type `@` followed by at least three characters to search for something to reference.

Search results can include:

- Entries
- Articles
- Properties
- Options for creating new content

Use the arrow keys to move through the results. Press `Enter` to insert the selected result, or `Escape` to close the search.

Select an existing reference to:

- Change its displayed name
- Open the referenced entry
- Add advanced reference options
- Remove the reference

Advanced options can link to a specific page or section. For example:

```text
page:abilities|anchor:#ability-1
```

Press `Enter` to save a change. Press `Escape` to cancel it.

Pressing `Backspace` directly after an entry reference changes it back to `@`, allowing you to search again.

## Links

To create a link:

1. Select the text that should become a link.
2. Select the link button or press `Ctrl+K` on Windows and Linux, or `Cmd+K` on macOS.
3. Enter the address.
4. Press `Enter`.

If the address has no protocol, the editor adds `https://`.

Select an existing link to:

- Change its address
- Open it in a new tab
- Remove the link

Submitting an empty address removes the link.

The editor also recognises links while you type or paste them.

## Lists

The editor supports:

- Bullet lists
- Numbered lists
- Task lists with checkboxes
- Nested lists and nested tasks

While editing a list:

| Key | Result |
|---|---|
| `Enter` | Create the next list item |
| `Tab` | Move the item into a nested level |
| `Shift+Tab` | Move the item out one level |
| `Backspace` on an empty item | Leave the list or join nearby content |

You can also start lists by typing:

```text
- Bullet item
* Bullet item
1. Numbered item
[ ] Task
[x] Completed task
```

Add a space after the marker to apply the formatting.

## Tables

Use `/table` to insert a table with:

- Two columns
- One header row
- Two content rows

Select one or more table cells to open the table menu. You can:

- Add a column after the selection
- Add a row after the selection
- Delete selected columns
- Delete selected rows
- Turn the header row on or off
- Add or remove borders
- Add or remove striped rows
- Position the table to the left or right
- Delete the table

Drag a column border to change its width. Wide tables can scroll horizontally.

While editing a table:

| Key | Result |
|---|---|
| `Tab` | Move to the next cell |
| `Shift+Tab` | Move to the previous cell |
| `Tab` in the final cell | Add a new row |
| `Backspace` or `Delete` with all cells selected | Delete the table |

## Images

You can add images in several ways:

- Use `/gallery` to choose an image from the gallery
- Use `/insert media` to upload an image
- Paste an image from your clipboard
- Paste a direct image URL
- Use image Markdown, such as `![Description](https://example.com/image.jpg)`
- Add an image through HTML source mode

Direct image URLs are recognised for common formats such as JPG, PNG, GIF, WebP, SVG, BMP, AVIF, and TIFF.

Select an image to open its menu. You can:

- Set its width to 25%, 50%, or 100%
- Reset its width
- Float it to the left
- Float it to the right
- Remove its floating position
- Delete it

You can also drag the handles around a selected image to resize it. The editor keeps the image proportions while resizing.

## Quotes, Code, and Dividers

### Quotes

Type `> ` at the beginning of a line to create a quote.

You can also select text and use the quote button or `/quote`.

### Code

Wrap text in backticks to create inline code:

```text
`example`
```

Start a code block by typing three backticks followed by a space or new line:

````text
```
````

You can also use `/code Block`.

### Dividers

Use `/horizontal rule`, or type one of these on an empty line:

```text
---
***
___
```

## Quick Formatting While Typing

The editor recognises several Markdown-style patterns:

| Type | Result |
|---|---|
| `**bold**` | Bold |
| `__bold__` | Bold |
| `*italic*` | Italic |
| `_italic_` | Italic |
| `~~strikethrough~~` | Strikethrough |
| `` `code` `` | Inline code |
| `==highlight==` | Highlight |
| `# Heading` | Heading level 1 |
| `## Heading` | Heading level 2 |
| `### Heading` | Heading level 3 |
| `> Quote` | Quote |
| `- Item` | Bullet list |
| `1. Item` | Numbered list |
| `[ ] Task` | Task list item |
| `---` | Divider |

Headings from level 1 to level 6 can be created by typing between one and six `#` characters followed by a space.

## Keyboard Shortcuts

On macOS, use `Cmd` where the table shows `Ctrl`. On Windows and Linux, use `Ctrl`.

### Text Formatting

| Windows and Linux | macOS | Result |
|---|---|---|
| `Ctrl+B` | `Cmd+B` | Toggle bold |
| `Ctrl+I` | `Cmd+I` | Toggle italic |
| `Ctrl+U` | `Cmd+U` | Toggle underline |
| `Ctrl+Shift+S` | `Cmd+Shift+S` | Toggle strikethrough |
| `Ctrl+E` | `Cmd+E` | Toggle inline code |
| `Ctrl+Shift+H` | `Cmd+Shift+H` | Toggle highlight |
| `Ctrl+Shift+B` | `Cmd+Shift+B` | Toggle quote |
| `Ctrl+Alt+C` | `Cmd+Alt+C` | Toggle code block |
| `Ctrl+K` | `Cmd+K` | Add a link to selected text |
| `Ctrl+Alt+0` | `Cmd+Alt+0` | Change to a paragraph |
| `Ctrl+Alt+1` | `Cmd+Alt+1` | Toggle heading level 1 |
| `Ctrl+Alt+2` | `Cmd+Alt+2` | Toggle heading level 2 |
| `Ctrl+Alt+3` | `Cmd+Alt+3` | Toggle heading level 3 |
| `Ctrl+Alt+4` | `Cmd+Alt+4` | Toggle heading level 4 |
| `Ctrl+Alt+5` | `Cmd+Alt+5` | Toggle heading level 5 |
| `Ctrl+Alt+6` | `Cmd+Alt+6` | Toggle heading level 6 |
| `Shift+Enter` | `Shift+Enter` | Insert a line break |
| `Ctrl+Enter` | `Cmd+Enter` | Insert a line break |

### Text Alignment

These shortcuts work with paragraphs and headings.

| Windows and Linux | macOS | Result |
|---|---|---|
| `Ctrl+Shift+L` | `Cmd+Shift+L` | Align left |
| `Ctrl+Shift+E` | `Cmd+Shift+E` | Align centre |
| `Ctrl+Shift+R` | `Cmd+Shift+R` | Align right |
| `Ctrl+Shift+J` | `Cmd+Shift+J` | Justify |

### Lists

| Windows and Linux | macOS | Result |
|---|---|---|
| `Ctrl+Shift+8` | `Cmd+Shift+8` | Toggle bullet list |
| `Ctrl+Shift+7` | `Cmd+Shift+7` | Toggle numbered list |
| `Ctrl+Shift+9` | `Cmd+Shift+9` | Toggle task list |

### History

| Windows and Linux | macOS | Result |
|---|---|---|
| `Ctrl+Z` | `Cmd+Z` | Undo |
| `Ctrl+Y` | `Cmd+Shift+Z` | Redo |

## HTML Source Mode

Use `/source` to edit the raw HTML.

When source mode opens, the editor tries to keep your position near the content you were editing. Select **Visual Editor** to return to the normal editor.

Source mode includes:

- HTML syntax highlighting
- Line numbers
- Search and replace
- Code folding
- Bracket matching
- Automatic indentation
- Multiple selections
- Line wrapping

Be careful when changing HTML. Invalid or incomplete HTML can change how the content appears.

### Source Mode Shortcuts

| Windows and Linux | macOS | Result |
|---|---|---|
| `Ctrl+F` | `Cmd+F` | Open search |
| `F3` or `Ctrl+G` | `F3` or `Cmd+G` | Next search result |
| `Shift+F3` or `Ctrl+Shift+G` | `Shift+F3` or `Cmd+Shift+G` | Previous search result |
| `Ctrl+Alt+G` | `Cmd+Alt+G` | Go to a line |
| `Ctrl+D` | `Cmd+D` | Select the next matching occurrence |
| `Ctrl+Shift+L` | `Cmd+Shift+L` | Select all matching occurrences |
| `Ctrl+Z` | `Cmd+Z` | Undo |
| `Ctrl+Y` | `Cmd+Shift+Z` | Redo |
| `Ctrl+/` | `Cmd+/` | Toggle an HTML comment |
| `Ctrl+[` | `Cmd+[` | Reduce indentation |
| `Ctrl+]` | `Cmd+]` | Increase indentation |
| `Tab` | `Tab` | Increase indentation |
| `Shift+Tab` | `Shift+Tab` | Reduce indentation |
| `Alt+Up` | `Alt+Up` | Move the current line up |
| `Alt+Down` | `Alt+Down` | Move the current line down |
| `Shift+Alt+Up` | `Shift+Alt+Up` | Copy the current line upward |
| `Shift+Alt+Down` | `Shift+Alt+Down` | Copy the current line downward |
| `Ctrl+Space` | `Ctrl+Space` | Open completion suggestions |
| `Shift+Ctrl+\\` | `Shift+Cmd+\\` | Move to the matching bracket |
| `Escape` | `Escape` | Close search, completion, or an extra selection |

There is no keyboard shortcut for leaving source mode. Select **Visual Editor** to return.
