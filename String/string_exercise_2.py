# จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "I am the best programmer"
string = "I am the best programmer"
print(len(string))

# จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "I am the best programmer"
string = "I am the best programmer"
print(string[0])

# จงเขียนคำสั่งเพื่อแสดง "best" ของข้อความ "I am the best programmer"
string = "I am the best programmer"
print(string[9:13])

# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ไม่มี space
a = "I"
b = "am"
c = "the"
d = "bast"
e = "programmer"
f = a + b + c + d + e
print(f)

# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมใหญ่ทั้งหมด
string = "I am the best programmer"
print(string.upper())

# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมเล็กทั้งหมด
string = "I am the best programmer"
print(string.lower())

# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ถูกแทนที่อักษร e ด้วย z ทั้งหมด
string = "I am the best programmer"
print(string.replace("e", "z"))

# จงเติมคำในช่องว่าเพื่อแสดงชื่อ
myname = "John"
txt = "{} is the best programmer"
print(txt.format(myname))