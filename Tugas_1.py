indeks = {
    "celcius " : "c",
    "kelvin " : "k",
    "fahrenheit " : "f",
    "reamur " : "r",
}
print("konversi suhu")
for i in indeks:
    print("satuan suhu :", i, "\t indeks : ", indeks[i])
     
suhu = float(input("masukan suhu : "))
satuan = input("masukan indeks konversi : ")

if (satuan == "c"):
    print(suhu, "derajat celcius :")
    print("reamur = ", (suhu*4/5))
    print("fahrenheit = ", (suhu*9/5)+32)
    print("kelvin = ", (suhu + 273))
elif (satuan == "k"):
    print(suhu, "derajat kelvin :")
    print("celcius = ", (suhu-273))
    print("fahrenheit = ", ((9/5)*(suhu-273) + 32))
    print("reamur = ", (4/5*(suhu-273)))
elif (satuan == "f"):
    print(suhu, "derajat fahrenheit :")
    print("celcius = ", (5/9)*(suhu-32))
    print("kelvin = ", (5/9)*(suhu-32)+273)
    print("reamur = ", (4/9 * (suhu-32)))
elif (satuan == "r"):
    print(suhu, "derajat reamur :")
    print("celcius = ", (suhu*5/4))
    print("kelvin = ", (suhu*5/4) + 273)
    print("fahrenheit = ", (suhu*9/4)+32)

