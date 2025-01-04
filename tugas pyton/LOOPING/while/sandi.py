print("Program Login")
print("ridwan andrian(211351144)")

password= "Python123"
salah= 0

while True:
    pw =str(input("Masukan Password: "))
    if password == pw:
        print("Login success")
        break
    else:
        print("Login failed") 
        salah += 1
        if salah == 3:
            print("akun terkunci")
            break
