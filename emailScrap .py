import re
import json

def start_scrap(text):
    email_list = re.findall(r"[\w\.]+@[\w\.]+\.\w{3}", text)
    # print(email_list)
    make_dict(email_list)

def make_dict(email_pool):
    email_occur = {}
    for email in email_pool:
        if email in email_occur:
            email_occur.update({email: email_occur[email] + 1})
            # email_occur[email]+=1
        else:
            email_occur.update({email: 1})
            # email_occur[email] = 1
    nested_json(email_occur)

def nested_json(email_occur):
    final_dict = {}
    for key, value in email_occur.items():
        type = email_category(key)
        # print(key,type,value)
        if type:
            final_dict.update({key: {"Occurance": value, "EmailType": type}})

    output_json = json.dumps(final_dict, indent=4)
    print(output_json)
    # B. final nested json output
    with open("result.json", "w", encoding="UTF-8") as output_file:
        json.dump(final_dict, output_file, indent=4)

def email_category(email):
    email_parts = email.split("@")
    email_prefix = email_parts[0]
    if "." in email_prefix:
        return "Human"
        # return Human email type if it is in the format firstname.lastname@email.com
    elif "." not in email_prefix and len(email_prefix) < 8:
        return "Non-Human"
        #return Non-human email type if its is in the format text@email.com where length of text<8

# A.Input: Given text with repeated email addresses
# plain_text = "Input Get 50% off on every purchase. contact marketing team at market@qq.com. And all your linkedin contacts for free, jeff.peterson@b2bsearch.com. qq.com partnership program apply at market@qq.com"
# start_scrap(plain_text)

# D. Testing Code: using provided dataset websiteData.txt
with open("websiteData.txt", "r", encoding="UTF-8") as file:
    file_text = file.read()
    start_scrap(file_text)
