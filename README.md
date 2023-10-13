# Log in as "admin"

- username: **dabzse**
- password: **localhost**

## Planned updates (something is visible right now):

- pagination (possible about 10 customers per page)
- adding profile photo (will require `pillow`)
  - modifying the model
  - and at least `customer/<pk>`
  - including the `views.py` file
- customer history
- some "better" design on `customer/<pk>`
- add logic to searchbox
- /etc

**YES, I KNOW!**\
in real life the customer's data is "deleted" only with the "soft-delete" method. so that means, it still exists in the database, but won't be visible... and that's against the law...

### Feel free to import this given `crm_customer.csv` into your SQLite3 database

it is given, you just need to import it.\
or use your own, whatever you like. for testing purposes SQLite3 is enough for me, and these very dummy data.

### If you would like to...

do it


## Currently in progress:

- paginator + design
