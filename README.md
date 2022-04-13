# Impact on Education

## Before you run it

This will not run properly without settings.py and db.sqlite3, both of which are absent from GitHub due to security issues. Check #f21-s22-ioe-missing-files in Slack for the files. **WHEN YOU PUSH YOUR CHANGES, KEEP THESE FILES ABSENT.**
## TODOs
### There are several TODOs throughout the document, marked as low, medium, or high priority.

- **Low**: Not the end of the world if these remain unfixed by production, but would be nice to fix. 
*(Bad code style, slightly messy pages, etc)*
- **Medium**: Must be fixed by production, but doesn't severely affect our ability to test the rest of the project.
*(Some security problems, things that should/shouldn't be accessible by certain users, etc)*
- **High**: Must be fixed before we can test the project properly, and absolutely must be fixed by production.
*(Missing homepages, URLs that don't go where they're supposed to, etc)*

### Finding where the TODOs are
#### In PyCharm: 
CMD+Shift+A, search for "TODO", then click on the one labeled `View | Tool Windows`
#### From Terminal:
Make sure your current directory is the project root.

Finding e.g. high priority TODOs:
`grep -rn "TODO (high priority)" *`

Finding all TODOs: `grep -rn "TODO (" *`

`grep -rn "TODO" *` won't work because there are some TODOs in Django's source code that will appear.

## Code style

### Type hints
Add type hints for the variables and functions you create, within reason. 
For example, `views.py` functions probably don't need any typehints. Rule of thumb:
If it makes the code more readable or your IDE more useful, add the typehint.

[Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) (highly recommend this)

[Official Python documentation for type hints](https://docs.python.org/3/library/typing.html)


### Document the relationship between views and templates
For each template you create, put a comment on the start saying which view(s) use this template. 
For each view you create, put a comment saying which template it uses, unless it's obvious 
(e.g. if it calls `render(request, "template.html")` or has `template_name="template.html" `). 
