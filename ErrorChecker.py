#!/path/to/python3
import sys
sys.path.append('LIBPATH')
from nightcheck import NightChecker
from emailer import Emailer
import os
import datetime
import re

#EMAIL_LIST = ['EMAIL@EMAIL.COM']
EMAIL_LIST = ['EMAIL1@domain.com','EMAIL2@domain.com']
table = ""

nc = ErrorChecker()
db,cursor = nc.get_db_info();
errors = nc.get_errors();
number = 0
subject = ""

for error in errors:
    if error != "None":
        number += 1

if errors:
    subject = "ERROR: Night Check"
    table = "<h4>The following scripts ran with errors:</h4>\n"
    table += """
        <table cellpadding='10'>
            <tr>
                <th>Caller</th>
                <th>Syntax Error</th>
                <th>Runtime Error</th>
            <tr>
    """

    for error in errors:
        #OKAY
        table += "<tr>"

        for ind, field in enumerate(error):
            if ind==0:
                field = field.rsplit('/',1)
                new_name = '</br>'.join(field)
                table += "<td>{}</td>".format(new_name)
            else:
                esc_field = re.sub(r'\\r\\n|\\r|\\n', '</br>', str(field))
                print("ESCAPED FIELD: \n\t|{}|".format(esc_field))
                table += "<td>{}</td>".format(esc_field)
        table += "</tr>"

    table+= "</table>"

if not errors:
    subject = "OKAY: Night Check"
    success = nc.get_okay();
    table = "<h4>The following scripts ran successfully:<h4>\n"
    table += """
        <table cellpadding='10'>
            <tr>
                <th>Execution Time</th>
                <th>Script Name</th>
            <tr>
    """
    for okay in success:
        table += """
            <tr>
                <td>{}</td>
                <td>{}</td>
            </tr>
        """.format(okay[0],okay[1])

new_email = Emailer(table, subject)
new_email.set_recipients(EMAIL_LIST)
new_email.send_email();

"""
nc.add_error("THIS IS URGENT",1);
"""
