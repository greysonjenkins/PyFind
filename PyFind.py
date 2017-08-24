# Project Name: PyFind
# Author: Greyson Jenkins


import re
import pyperclip

matches = []


def extractLinks(text):

    linkRegex = re.compile(r'''
        \s                                     # By searching for a space before the link, the regex will not mistake the final part of an email for a link
        (http:\/\/|https:\/\/)?                # Search for protocol (optional)
        (www\.)?                               # Search for www. (optional)
        ([a-z0-9]*)                            # Search for domain name of any length (required)
        (\.)                                   # Search for . (required)
        (com|net|org|gov|edu|io|xyz|co)        # Search for domain type (required)
        (\/[a-z0-9\.\/\#\?\%\=\_]*)?           # Search for URL path to specific page (optional)
        ''', re.IGNORECASE | re.VERBOSE)       # re.IGNORECASE ignores whether a letter is capitalized or lower case. re.VERBOSE ignores whitespace
                                               # and allows for comments

    links = linkRegex.findall(text) # Search text using linkRegex regular expression, store the matches in the links varbiable

    # Iterates through each tuple in the list returned by .findall()
    for group in links:

            link = ''.join(group) # Join all strings in each tuple

            if link in matches: # If a link is already stored in the match list, it is ignored
                pass

            else:
                matches.append(link) # Append joined tuple to list


def extractPhones(text):

    phoneRegex = re.compile(r'''
        (\d\d\d|\(\d\d\d\))?      # area code
        (\s|-|\.)?                # separator
        (\d\d\d)                  # first 3 digits
        (\s|-|\.)                 # separator
        (\d\d\d\d)                # last 4 digits
        ''', re.VERBOSE)

    phones = phoneRegex.findall(text)
    print(phones)

    for phoneNum in phones:

        phoneNumber = ''.join(phoneNum)
        phoneNumber = phoneNumber.strip()

        if phoneNumber in matches:
            pass

        else:
            matches.append(phoneNumber)


def extractEmails(text):

    emailRegex = re.compile(r'[a-z0-9\.\_]*\@[a-z0-9]*\.com', re.VERBOSE | re.IGNORECASE)

    emails = emailRegex.findall(text)

    for email in emails:

        if email in matches:
            pass

        else:
            matches.append(email)


regexDict = {'links': extractLinks,
             'emails': extractEmails,
             'phones': extractPhones}


extractFrom = pyperclip.paste()

validInput = False

while validInput == False:

    print("What would you like to extract? Separate items with spaces")
    toExtract = input("> ")

    toExtract = toExtract.split()

    for item in toExtract:

        if item in regexDict:
            validInput = True
            regexDict[item](extractFrom)

        else:
            print("\nInvalid parameter detected. Please try again.")


matches = '\n'.join(matches)

pyperclip.copy(matches)

print("\nCopied to clipboard\n------------------")
print(matches)
