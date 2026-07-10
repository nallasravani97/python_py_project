# Student Discount(AND)
student_details = {"Age": 27,
    "has_id" : True}
if  student_details["Age"] < 18 and student_details["has_id"]:
    print("Age is less than 18")
else:
    print("You are eligible for discount")
# Promo code(OR)
is_new_user = False
has_promo = True
if is_new_user or has_promo:
    print("Discount Applied")
else:
    print("No Discount")
# Parental Consent (NOT)
age = 20
if not (age>18):
    print("Parental Consent Required")
else:
    print("No Parental Consent Required")