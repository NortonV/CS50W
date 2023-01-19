# To do list

2. **New Page**: Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry.
* Users should be able to enter a title for the page and, in a [textarea](https://www.w3schools.com/tags/tag_textarea.asp), should be able to enter the Markdown content for the page.
* Users should be able to click a button to save their new page.
* When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.
* Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.

3. **Edit Page**: On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea.
* The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).
* The user should be able to click a button to save the changes made to the entry.
* Once the entry is saved, the user should be redirected back to that entry’s page.