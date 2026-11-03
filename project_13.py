# phonenumber 

import phonenumbers
from phonenumbers import geocoder,carrier


number = input("enter phone number :")

try :
    phone = phonenumbers.parse(number,None)


    if phonenumbers.is_valid_number(phone):
        print("Vaild phone number")

        region = geocoder.description_for_number(phone,"en")
        print("Region:",region)

        network = carrier.name_for_number(phone,"en")
        print("carrier :" , network or "not available")

        print("international format :",
              phonenumbers.format_number(
                  phone,
                  phonenumbers.phonenumberformat.INTERNATIONAL))
    else:
        print("invalid phone number")
except phonenumbers.NumberParseException:
    print("please enter a valid number with country code .")