# Tawtai morilno uu hewleh
print("Тавтай морилно уу?")

# Hereglegchees neriig ni garaas awah
name = input("Эрхэм хэрэглэгч та нэрээ оруулна уу: ")

# Nereer ni mendleed nasiig ni awah
print(f"Өдрийн мэнд, {name}!")
age = int(input("Та одоо хэдэн настай вэ?: "))

# Hereglegch hezee 100 nas hurehiig tootsoolj hewlej haruulah
torson_jil = 2025 - age
zuun_nas_hureh_jil = torson_jil + 100
if age < 100:
   print(f"Хэрэглэгч {name} та {zuun_nas_hureh_jil} онд 100 нас хүрэх юм байна")
   print("Танд амжилт хүсье!")
else :
   print(f"Алдаа гарлаа! Tа дахиж 100н насныхаа парти-г хийх боломжгүй байна")