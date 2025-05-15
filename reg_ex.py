from re import match


phone = input("Telefon raqamni kiriting: ")
pattern = "^[+]998[0-9]{9}$"

print(match(pattern, phone))


"""
link -> https://docs.python.org/3/howto/regex.html
link -> https://docs.python.org/3/library/re.html
link -> https://www.w3schools.com/python/python_regex.asp

RegEx funksiyalari
match()     -   Solishtirish uchun  
findall()   -   Barcha mosliklarni o'z ichiga olgan ro'yxatni qaytaradi
search()    -   Agar matnning istalgan joyida moslik mavjud bo'lsa, Match ob'ektini qaytaradi

\w - So'z belgilari -->  a-z / A-Z 
\d - Raqam  --> 0-9
\b - So'z chegarasi --> $
\s - bo'shliq
^  - boshlanish

"""

ism = input("'L' bilan boshlanadigan va 6 ta harifli ism kiriting: ")
pattern2 = "^L[a-z]{5}$"
print(match(pattern2, ism.title()))

from re import findall, search

phone_number_pattern = r"[+]998[(][0-9]{2}[)][\s][0-9]{3}-[0-9]{2}-[0-9]{2}"
car_pattern3 = r"[0-9]{2}[\s][A-Z][0-9]{3}[A-Z]{2}"

matn1 = """
    Bugun kun quyoshli va issiq bo'lyapdi. Mahzuna dadasining mashinasida maktabga keldi. 
    Mashinaning raqami 50 A327CB ed. Uning dugonasi Oydina esa 40 V456AA raqamli mashinada keldi.
    Maftuna yangi telefon raqami oldi u +998(90) 545-50-75 edi.  Uning oldingi raqami esa 
    +998(95) 963-12-81 edi. Oyisiniki esa +998(55) 325-65-95 bo'lgan.
"""

""" findall() """
print(findall(car_pattern3, matn1))
print(findall(phone_number_pattern, matn1))


""" search() """
print(search(phone_number_pattern, matn1))
print(search(car_pattern3, matn1))


word = input("Enter a word: ")
word_regex = r"^[\w]{5,10}$"
print(match(word_regex, word))

matn = """Assalomu aleykum #python  Salima 17 do’kon  Kamalak  ranglari,
 12345 #assalomu-aleykum 
 Saida aqilli 998 imtihon Rayhona ajoyib #shunchaki 
 #hobby 7786 Sevara chiroyli 7777777 Suhrob"""


"""
1-mashq | 10 Ball
AD 2359875 | JH 434-45 S  shular uchun RegEx tuzing

2-mashq | 10 Ball | findall()
  Matndan faqat 7 ta harfli so’zlarni ajratib oling

3-mashq | 10 Ball | findall()
Matndan barcha # bilan boshlangan 12 ta belgigacha bo’ladigan so’zlarni topib bering.

4-mashq | 10 Ball | search()
Matndan faqat 5 honagacha bo’lgan birinchi sonani ajratib oling.

5-mashq | 10 Ball
Matndan eng birinchi “S“ harfi bilan boshlanib “a” bilan tugagan ismni topib bering
"""

from re import match, findall, search
""" 1 """
print(match("^[A-Z]{2}[\s][0-9]{7}$", "AD 2359875"))
print(match("^[A-Z]{2} [0-9]{3}-[0-9]{2} [A-Z]$", "JH 434-45 S"))


""" 2 """
print(findall('[A-Za-z]{7}', matn))

""" 3-mashq """
print(findall("[#][A-Za-z]{1,12}", matn))

"""4-mashq"""
print(search('[0-9]{1,5}', matn))

"""5-mashq"""
print(search('S[a-z]{1,10}a', matn))
