import speech_recognition as spr   # importando a biblioteca

rec = spr.Recognizer()

with spr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print(".")
    ad = rec.listen(mic)  # audio
    txt = rec.recognize_google(ad, language="pt-BR")  # texto
    

# fala reconhecida e respondida
if txt == "Oi":
    print("Oie!")
    print("Qual é o seu nome?")

with spr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print(".")
    ad = rec.listen(mic)
    name = rec.recognize_google(ad, language="pt-BR")

    print("Como vai " + name + "?")

try:
    with spr.Microphone() as mic:
     rec.adjust_for_ambient_noise(mic)
     print(".")
     ad2 = rec.listen(mic)
     txtres = rec.recognize_google(ad2, language="pt-BR")


    if txtres == "estou bem" or txtres == "vou bem":
       print("QUE BOM")
    elif txtres == "estou triste" or txtres == "vou mal": 
       print("Não fique assim, você é tão especial!")
except Exception as v:
    print("Erro:", v)






    

