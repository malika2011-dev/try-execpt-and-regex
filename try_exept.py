""" try-except   --> xatoliklarni oldini olish """

""" 1-mashq """
def yosh_top(t_yil:int) -> int:
    """  """
    from datetime import date
    
    try:
        return f"Siz {date.today().year - t_yil} yoshdasiz !"
    except:
        return f"Yosh topishda xatolik bo'ldi !!!"


print(yosh_top(1866))
print(yosh_top(2006))
print(yosh_top("2022"))

print("Dastur hali tugamadi, u davom etadi !")


""" 2-mashq """
try:
    son1 = int(input("1-sonni kiriting: "))
    son2 = int(input("2-sonni kiriting: "))

    print(f"{son1} : {son2} = {son1/son2}")
except ValueError:
    print(f"Xatolik !!! \nSiz faqat son kiritshingiz shart !")
except ZeroDivisionError:
    print(f"Xatolik !!! \nSonni 0 ga bo'lib bo'lmaydi !")
except:
    print(f"Xatolik !!! \nQaytadan urinib ko'ring !")
    
    
"""
https://www.tutorialsteacher.com/python/error-types-in-python

AssertionError -     Assert bayonoti bajarilmaganda ko'tariladi.
AttributeError -     Atribut tayinlashda ko'tarildi yoki mos yozuvlar bajarilmadi.
EOFError -   Input() funksiyasi faylning oxiri holatiga tushganda ko'tariladi.
FloatingPointError -     Suzuvchi nuqta operatsiyasi bajarilmaganda ko'tariladi.
GeneratorExit -  Jeneratorning close() usuli chaqirilganda ko'tariladi.
ImportError -     xatosi Import qilingan modul topilmaganda ko'tariladi.
IndexError -     Ketma-ketlik indeksi diapazondan tashqarida bo'lganda ko'tariladi.
KeyError -   Kalit lug'atda topilmasa ko'tariladi.
KeyboardInterrupt -  Foydalanuvchi uzilish tugmachasini bosganda ko'tariladi (Ctrl+c yoki o'chirish).
MemoryError -    Operatsiya xotirasi tugashi bilan ko'tariladi.
NameError -  O'zgaruvchi mahalliy yoki global miqyosda topilmasa ko'tariladi.
NotImplementedError -    Mavhum usullar bilan ko'tarilgan.
OSError -    Tizim ishi tizim bilan bog'liq xatolikka sabab bo'lganda ko'tariladi.
OverflowError -  Arifmetik amal natijasi koʻrsatish uchun juda katta boʻlganda koʻtariladi.
ReferenceError -     Axlat yig'ilgan referentga kirish uchun zaif havola proksi-serverdan foydalanilganda ko'tariladi.
RuntimeError -   Xato boshqa toifaga kirmasa ko'tariladi.
StopIteration -  iterator tomonidan qaytariladigan boshqa element yo'qligini bildirish uchun keyingi() funktsiyasi tomonidan ko'tariladi.
SyntaxError -    Sintaksis xatosiga duch kelganda tahlilchi tomonidan ko'tariladi.
IndentationError -   Noto'g'ri chiziq mavjud bo'lganda ko'tariladi.
TabError -   Qachonki chekinish mos kelmaydigan yorliqlar va bo'shliqlardan iborat bo'lsa ko'tariladi.
System -  xatosi Tarjimon ichki xatoni aniqlaganida ko'tariladi.
SystemExit -     sys.exit() funksiyasi tomonidan ko'tarilgan.
TypeError -  Funktsiya yoki operatsiya noto'g'ri turdagi ob'ektga qo'llanilganda ko'tariladi.
UnboundLocalError -  Funksiya yoki usulda mahalliy o‘zgaruvchiga havola qilinganda ko‘tariladi, lekin bu o‘zgaruvchiga hech qanday qiymat bog‘lanmagan.
UnicodeError -   Unicode bilan bog'liq kodlash yoki dekodlash xatosi yuzaga kelganda ko'tariladi.
UnicodeEncodeError -     Kodlash paytida Unicode bilan bog'liq xatolik yuzaga kelganda ko'tariladi.
UnicodeDecodeError -     Unicode bilan bog'liq xato dekodlash vaqtida yuzaga kelganda ko'tariladi.
UnicodeTranslateError -  Unicode bilan bog'liq xato tarjima paytida yuzaga kelganda ko'tariladi.
ValueError -     Funktsiya to'g'ri turdagi, lekin noto'g'ri qiymatdagi argumentni olganida ko'tariladi.
ZeroDivisionError -  Bo'linish yoki modul operatsiyasining ikkinchi operandi nolga teng bo'lganda ko'tariladi.


"""
"""1-mashq"""

sonlar = [0, 5, 10, 15, 25]

try:
    savol = int(input("Biror son kiriting: "))
    for son in sonlar:
        try:
            print(f"{savol}:{son}={savol/son}")
        except ZeroDivisionError:
            print(f"Sonni 0 ga bo'lib bo'lmaydi !")
        
except ValueError:
    print("Siz faqat son kirita olasiz !")
except:
    print(f"Xatolik bor iltimos qaytadan urinib ko'ring !")




"""2-mashq"""

def yosh() -> list:
    """ """

    bolinadiga_sonlar = []
    sonlar2 = list(range(1, 1001))

    try:
        yosh = int(input("Yoshingizni kiriting: "))
   
        for son in sonlar2:
            if son % yosh == 0:
                bolinadiga_sonlar.append(son)
    
        print("Bu sonlar qoldiqsiz bo'linadi !")
        print(bolinadiga_sonlar)
    except ValueError:
        print("xatolik !!! Siz faqat son kiritishingiz kerak !")
    except:
        print("xatolik !!! Qaytadan urining")

yosh()



"""3-mashq""" 
mevalar = ["olma", "banan", "nok", "gilos", "ananas", "shaftoli"]

try:
    mevalar.remove("ol")
    mevalar.remove("banan")
except ValueError:
    print(f"Siz yo'q narsani o'chirishga urindingiz !")

try:
    del mevalar[220] 
    del mevalar[1] 
except IndexError:
    print(f"Siz yo'q indexni kiritdingiz !")


print("Qolgan mevalar:")
print(mevalar)

mevalar.append("olcha")
mevalar.append("kivi")
mevalar.append("limon")
mevalar.append("apelsin")
mevalar.append("mandarin")

print("Yangi mevalar:")
print(mevalar)

del mevalar

try:
    mevalar.clear()
except NameError:
    print("Siz o'zgaruvchini nomini yozishda xatolikka yo'l qo'ydingiz !")
