# importando a bibliotecas
import speech_recognition as spr 
import pyautogui as pag

rec = spr.Recognizer()

with spr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print(".")
    ad = rec.listen(mic)  # audio
    txt = rec.recognize_google(ad, language="pt-BR")  # texto
    
    print("")
    print("Resposta do usuário: " +txt)
# fala reconhecida e respondida
if txt == "Oi":
    print("Oie!")
    print("Qual é o seu nome?")


with spr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print(".")
    ad = rec.listen(mic)
    name = rec.recognize_google(ad, language="pt-BR")

    print("")
    print("Resposta do usuário: " +name)

    print("Como vai " + name + "?")


try:
    with spr.Microphone() as mic:
     rec.adjust_for_ambient_noise(mic)
     print(".")
     ad2 = rec.listen(mic)
     txtres = rec.recognize_google(ad2, language="pt-BR")


    print("")
    print("Resposta do usuário: " +txtres)


    if txtres == "estou bem" or txtres == "vou bem":
       print("QUE BOM")
    elif txtres == "estou triste" or txtres == "vou mal" or txtres == "estou mal": 
       print("Não fique assim, você é tão especial!")
except Exception as v:
    print("Erro:", v)

print("")
print("O que deseja fazer hoje?")
print("- Abrir Excel;")
print("- Abrir Google;")
print("- Abrir Notcias")

with spr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print(".")
    ad = rec.listen(mic)
    tarefa = rec.recognize_google(ad, language="pt-BR")

    print("")
    print("Resposta do usuário: " +tarefa)

    
    if tarefa == "abrir excel":
       
        pag.PAUSE = 1

        # apertar a tecla do windows 
        pag.press("win")
        # digita o nome do programa
        pag.write("excel")
        # aperta enter
        pag.press("enter")

    
       





    

