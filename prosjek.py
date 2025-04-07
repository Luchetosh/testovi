print("Matematika\n"
      "Engleski\n"
      "Povijest\n"
      "Hrvatski\n"
      "Geografija\n"
      "Materijali\n"
      "Vjeronauk\n"
      "OET\n"
      "Fizika\n"
      "Tjelesno\n"
      "Racunalstvo:\n"
      "Mjerenje:\n"
      "Radionicke:\n"
      "Finomehanika:\n"
      "--- 𝕌𝕟𝕖𝕤𝕚 𝕤𝕧𝕠𝕛𝕖 𝕠𝕔𝕛𝕖𝕟𝕖 --->")

def predmeti():
    Matematika = int(input("Matematika: "))
    Engleski = int(input("Engleski: "))
    Povijest = int(input("Povijest: "))
    Hrvatski = int(input("Hrvatski: "))
    Geografija = int(input("Geografija: "))
    Materijali = int(input("Materijali: "))
    Vjeronauk = int(input("Vjeronauk: "))
    Oet = int(input("OET: "))
    Fizika = int(input("Fizika: "))
    Tjelesno = int(input("Tjelesno: "))
    Racunalstvo = int(input("Racunalstvo: "))
    Mjerenje = int(input("Mjerenje: "))
    Radionicke = int(input("Radionicke: "))
    Finomehanika = int(input("Finomehanika: "))
    zbroj = (
            Matematika + Engleski + Povijest + Hrvatski + Geografija +
            Materijali + Vjeronauk + Oet + Fizika + Tjelesno +
            Racunalstvo + Mjerenje + Radionicke + Finomehanika 
            )
    return zbroj

prosjek = predmeti() / 14
print(f"Prosjek {prosjek: .2f}")