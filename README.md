# ErrorChecker
NightChecker developed to automate the process of going into every script to check for errors. An email is sent out to me every morning with an OK or an Error subject to let me know which scripts/ applications failed overnight. This class is incorporated throughout various tools

If there are a lot of scripts, it cant be painstaking and time consuming to check that every single script is working. This was an issue for me, so I decided to make a script that iterates through the logs to see if there are any issues that occured during runtime. Similarly, syntax errors are checked.
Adding scripts to be checked can be done through the DIRECTORIES_TO_CHECK variable.

Future changelog:
    - Add logic to catch operational errors.
