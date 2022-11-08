# Mailchimp Data Querying App
Python console app for handling common data queries using Mailchimp's API.

## App goals
This app is designed to help Sport Wales marketers and communicators generate data reports not currently available through the standard Mailchimp website UI.

## Warning
You will not find an API key anywhere in this repository or commit history. You will need to retrieve this key from the Mailchimp account and host it in an environmental variable or only run the app locally.

**Do not** commit the API key and do not save it on any non-work cloud networks.

## Set up
This app runs directly from user input in the console. Simply run the script in your terminal to begin the program.
``
python3 src/mailchimp_app/app.py 
```

You will need to make sure you have the mailchimp_marketing python library installed via pip:
```
pip install marketing_manager
```

Alternatively, you can clone the source code for the library directly:
```
pip install git+https://github.com/mailchimp/mailchimp-marketing-python.git
```

Once this is installed the python app files can import it.

## Documentation
- [Connecting to Mailchimp's API](https://mailchimp.com/developer/marketing/docs/fundamentals/#connecting-to-the-api)
- [Mailchimp's API Reference Guide](https://mailchimp.com/developer/marketing/api/)
- [Mailchimp API Python library](https://github.com/mailchimp/mailchimp-marketing-python)
