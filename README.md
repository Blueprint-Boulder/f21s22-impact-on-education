# Impact on Education

## Before you run it

This will not run properly without settings.py and db.sqlite3, both of which are absent from GitHub due to security issues. Check the pins in #f21-s22-ioe for the files. **WHEN YOU PUSH YOUR CHANGES, KEEP THESE FILES ABSENT.**
## TODOs
### There are several TODOs throughout the document, marked as low, medium, or high priority.

- **Low**: Not the end of the world if these remain unfixed by production, but would be nice to fix. 
*(Bad code style, slightly messy pages, etc)*
- **Medium**: Must be fixed by production, but doesn't severely affect our ability to test the rest of the project.
*(Some security problems, things that should/shouldn't be accessible by certain users, etc)*
- **High**: Must be fixed before we can test the project properly, and absolutely must be fixed by production.
*(Missing homepages, URLs that don't go where they're supposed to, etc)*

### Finding where the TODOs are
#### In Pycharm: 
CMD+Shift+A, search for "TODO", then click on the one labeled `View | Tool Windows`
#### From Terminal:
Make sure your current directory is the project root.

Finding e.g. high priority TODOs:
`grep -rn "TODO (high priority)" *`

Finding all TODOs: `grep -rn TODO (" *`

`grep -rn "TODO" *` won't work because there are some TODOs in Django's source code that will appear.

## Code style

### Type hints
Please add type hints for all variables and functions you create, with the exception of return types and arguments for `views.py` functions or overridden functions.

[Python documentation for type hints](https://docs.python.org/3/library/typing.html)

Example type hints:

```python
def hi(times):
    output = ""
    for i in range(0, times):
        output += "hi"
    return output
```

becomes

```python
def hi(times: int) -> str:
    output: str = ""
    for i in range(0, times):
        output += "hi"
    return output
```

### Document the relationship between views and templates
For each template you create, put a comment on the start saying which view(s) use this template. 
For each view you create, put a comment saying which template it uses, unless it's obvious (e.g. if it calls `render(request, "template.html")` ). 
It might not be obvious if the view is a class 
(e.g. `ApplicationUpdateView` in `applicant/views.py`).




## Making the users table (UNFINISHED)
### Please make the users table in `users/templates/users/userInfo.html`.

### API for the users table:
#### Variables:
- `users`: A set containing every user on the website. You can iterate through it with a standard for loop. Each user is a `CustomUser`.

#### Classes:

`CustomUser`: Represents a user.

- Instance variables (for a given instance of `CustomUser` called `user`):
  - `user.application_set.all`: A set of `Application`s representing every application the user has started, submitted or not. You can iterate through it with a standard for loop.

`Application`: Represents a user's application. A user can have several applications.
- Instance variables (for a given instance of `Application` called `app`):
  - `app.author`: The `CustomUser` that `app` was written by.
  - `app.text`: A string representing the full text of the application. Has a maximum length of 5000 characters.
  - `app.submitted`: A boolean representing whether the user has submitted the application.
  - `app.review`: The `Review` associated with `app`. `None` if it has not been reviewed.

`Review` (TBD): Represents a review of an application. An application can only have one review.
- Instance variables (for a given instance of `Review` called ` review`):
  - `review.author`: The `CustomUser` that `review` was written by.
  - `review.application`: The `Application` associated with the review.
  - `review.text`: A string representing the full text of the review.
  - `review.submitted`: A boolean representing whether the volunteer has submitted the review.
#### Some things you can link to:

See `users/templates/users/exampleUserInfo.html` for an example of how you could use all of these features.




