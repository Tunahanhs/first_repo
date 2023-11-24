matematik = input("Matematik notunuzu yazınız ")
turkce = input("türkçe notunuzu yazınız ")
sosyal = input("sosyal notunuzu giriniz ")
edebiyat =input("edebiyat notunuzu giriniz ")
ortalama = (float(matematik) + float(turkce) + float(sosyal) + float(edebiyat)) / 4
print(f"not ortalamanız {ortalama}'dır.")
