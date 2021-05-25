Users=[{"user": "Jose", "access_level": "admin"},
       {"user": "Liv", "access_level": "guest"}]

print("Decorator without @ notation")
print("============================")
def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_get_admin():
        for user in Users:
            if(user["access_level"] == "admin"):
                 print(func)
            else:
                print(f"No admin access has ben provided to {user['user']}")

    return(secure_get_admin)

get_admin_pwd = make_secure(get_admin_password())
get_admin_pwd()
print(f"The name of the function which is being decotrated: {get_admin_password.__name__}")

print()

"""decorator with @ notation
Drawback:- the function being decorated looses its name and documentation if any at the time of getting replaced.
Its name does not get registered with python. but using functool.wrap() helps us to retain the decorating function's name"""

print("Decorator @ notation")
print("============================")
#import functools
def make_secure(func):
   # @functools.wraps(func)
    def secure_get_admin():
        for user in Users:
            if(user["access_level"] == "admin"):
                 print(func())
            else:
                print(f"No admin access has ben provided to {user['user']}")

    return(secure_get_admin)

@make_secure
def get_admin_password():
    return "1234"

get_admin_password()
print(f"The name of the function which is being decotrated: {get_admin_password.__name__}")
