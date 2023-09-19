memedict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "leggera disapprovazione",
            "CREEPY": "spaventoso, inquietante",
            "PARA": "preoccuparsi per qualcosa, paranoiarsi",
            }
parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
while parola != "STOP":
    if parola in memedict.keys():
        print(parola, memedict[parola])
    else:
        print("Mo' però ci sono due opzioni: 1: Non sono completo fra'; 2: Hai scritto male, hai scritto tutto MAIUSCOLO?")
