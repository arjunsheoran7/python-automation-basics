role = input("Enter user role: ").strip().lower()
if role == "admin":
    print("Full access granted")
else:
    print("Limited access granted")