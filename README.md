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




## What to do if the migrations files and/or database are messed up (e.g. if you accidentally refactored stuff in them)

### Removing the problem files

1. Remove all files from all migrations folders except the `__init__.py` files.

2. ***NOTE:** If you stored anything important in the database that you really do not want to lose, try only following Step 1 in* "Removing the problem files" *and Step 1 in* "Setting up the database again". *If that doesn't work, I unfortunately don't know of any way to fix it other than following this step.*

   Delete the database file (`db.sqlite3`). Do not refactor anything when you delete it (in PyCharm, this means unchecking "Safe Delete").

### Setting up the database again

1. Make sure you're in the project's root directory. Run `python manage.py makemigrations`, then run `python manage.py create_database`. If `python manage.py makemigrations` doesn't work, then something is wrong with your code, not just the database or migrations files. If `python manage.py create_database` doesn't work, you likely didn't follow the steps in *Removing the problem files*.
2. Run `python manage.py createsuperuser` and follow the prompts. This will create a user that can access Django's admin site.
3. Run your project and go to Django's admin site (located in `/admin`). Login as the user you just created.
4. Add the following groups: *student, volunteer, org_admin,* and *site_admin*. Give *site_admin* all permissions. It doesn't matter (for testing purposes) which permissions the other groups have.

### Testing to make sure this didn't break anything else

1. Make an account of each user type (using the "create account" page at `/accounts/register`). If you get the error `The CustomUser could not be created because the data didn't validate.`, this probably isn't a sign that the site is broken; it means you entered a username that already exists, or the email wasn't valid, or the password was too weak, or the passwords didn't match, etc.
2. Login as each of those accounts and make sure they work properly. 


## Making the users table (UNFINISHED)
### Please make the users table in `org_admin/templates/org_admin/users.html`.

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
  - `app.submitted`: A boolean representing whether the user has submitted the application.
  - `app.review`: The `Review` associated with `app`. `None` if it has not been reviewed.

`Review` (TBD): Represents a review of an application. An application can only have one review.
- Instance variables (for a given instance of `Review` called ` review`):
  - `review.author`: The `CustomUser` that `review` was written by.
  - `review.application`: The `Application` associated with the review.
  - `review.text`: A string representing the full text of the review.
  - `review.submitted`: A boolean representing whether the volunteer has submitted the review.
