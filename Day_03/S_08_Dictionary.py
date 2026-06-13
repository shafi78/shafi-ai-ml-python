# Dictionary

info = {
    "name": "shafi",
    "lang":"java"
}


print(info)

print(info["name"])  # shafi


# keys()

print(info.keys())  # dict_keys(['name', 'lang'])


#values()

print(info.values()) # dict_values(['shafi', 'java'])


# items()

print(info.items())  # dict_items([('name', 'shafi'), ('lang', 'java')])


# get()

print(info.get("name"))  # shafi
print(info.get("nam"))   # None (return None if not found)


# update()

info.update({
    "city":"Bengaluru"
})

print(info)