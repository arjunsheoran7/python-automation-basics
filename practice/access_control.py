role = input("Enter user role: ").strip().lower() #normalization
if role == "admin":
    print("Full access granted")
else:
    print("Limited access granted")