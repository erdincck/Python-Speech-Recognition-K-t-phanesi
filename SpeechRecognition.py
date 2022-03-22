
# Kütüphanenin import edilmesi
import speech_recognition as sr
import time

start = time.time()

#recognizer sınıfının tanıtılması
sestani = sr.Recognizer()

#Kayıdın okutulması
with sr.AudioFile('deneme.wav') as kaynak:

    metin = sestani.listen(kaynak)

    try:
        # Google ses tanıma servisini kullan
        text = sestani.recognize_google(metin, language = "tr-TR")
        print('Ses metni:')
        print(text)

    except:
         print('Bir hata oluştu, üzgünüm.')
end1 = time.time()
süre=end1 - start
print("Dönüştürme süresi",süre) 



