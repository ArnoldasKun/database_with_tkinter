from sqlalchemy.orm import sessionmaker
from model import engine, Stotis, Puolejas, Regionas, Dalyviai, Datos

session = sessionmaker(bind=engine)()


def stociu_lentele():
    print("=== Stociu sarasas ===")
    print("#, Sistema, Pavadinimas, Tipas, Aljansas, Korporacija")
    duomenys = session.query(Stotis).all()
    for duomenys in duomenys:
        print(duomenys)

def regiono_lentele():
    print("/// Regionas ///")
    print("#, Pavadinimas")
    duomenys = session.query(Regionas).all()
    for duomenys in duomenys:
        print(duomenys)

def puoleju_lentele():
    print("... Puoleju duomenys ...")
    print("#, Aljansas, Korporacija")
    duomenys = session.query(Puolejas).all()
    for duomenys in duomenys:
        print(duomenys)

def dalyviu_lentele():
    print("+++ Dalyviai +++")
    print("#, Vardas, Ismoka")
    duomenys = session.query(Dalyviai).all()
    for duomenys in duomenys:
        print(duomenys)

def datu_lentele():
    print("*** Laikas ***")
    print("#, Apleidimo laikas, Puolimo laikas")
    duomenys = session.query(Datos).all()
    for duomenys in duomenys:
        print(duomenys)

def nauja_stotis():
    print("==== Nauja stotis ====")
    try:
        sistema = input("Iveskite sistema: ")
        pavadinimas = input("Iveskite pavadinima: ")
        tipas = input("Iveskite tipa: ")
        aljansas = input("Iveskite aljansa: ")
        korporacija = input("Iveskite korporacija: ")
    except ValueError:
        print("B***, nedrebink ranku.")
        return
    else:
        irasas = Stotis(sistema, pavadinimas, tipas, aljansas, korporacija)
        session.add(irasas)
        session.commit()
        print(f"Stotis {irasas} prideta i sarasa.")

def naujas_regionas():
    print("//// Naujas regionas ////")
    try:
        pavadinimas = input("Iveskite pavadinima: ")
    except ValueError:
        print("B***, nedrebink ranku.")
        return
    else:
        irasas = Regionas(pavadinimas)
        session.add(irasas)
        session.commit()
        print(f"Regionas {irasas} irasytas sekmingai.")

def naujas_puolejas():
    print(".... Naujas puolejas ....")
    try:
        aljansas = input("Iveskite aljansa: ")
        korporacija = input("Iveskite korporacija: ")
    except ValueError:
        print("B***, nedrebink ranku.")
        return
    else:
        irasas = Puolejas(aljansas, korporacija)
        session.add(irasas)
        session.commit()
        print(f"Maitedos {irasas} prideti.")

def naujas_dalyvis():
    print("++++ Naujas dalyvis ++++")
    try:
        vardas = input("Iveskite varda: ")
        ismoka = input("iveskite isk: ")
    except ValueError:
        print("B***, nedrebink ranku.")
        return
    else:
        irasas = Dalyviai(vardas, ismoka)
        session.add(irasas)
        session.commit()

def naujas_data():
    print("**** Naujas laikas ****")
    try:
        apleidimo_laikas = input("Iveskite apleidimo laika: ")
        puolimo_laikas = input("Iveskite puolimo laika: ")
    except ValueError:
        print("B***, nedrebink ranku.")
        return
    else:
        irasas = Datos(apleidimo_laikas, puolimo_laikas)
        session.add(irasas)
        session.commit()

def ivedimas_stociu():
    stociu_lentele()
    try:
        stotis_id = int(input("Iveskite stoties ID: "))
    except ValueError:
        print("B***, tai turi buti skaicius.")
        return
    else:
        if stotis_id:
            irasas = session.query(Stotis).get(stotis_id)
            if irasas:
                return irasas
            else:
                print(f"B***, stotis su ID: {stotis_id} neegzistuoja")
                return

def atnaujinti_stotis():
    irasas = ivedimas_stociu()
    if irasas:
        try:
            sistema = input(f"Sistema ({irasas.sistema}): ")
            pavadinimas = input(f"Pavadinimas ({irasas.pavadinimas}): ")
            tipas = input(f"Tipas ({irasas.tipas}): ")
            aljansas = input(f"Aljansas ({irasas.aljansas}): ")
            korporacija = input(f"Korporacija ({irasas.korporacija}): ")
        except ValueError:
            print("B***, nedrebink ranku.")
        else:
            if len(sistema) > 0:
                irasas.sistema = sistema
            if len(pavadinimas) > 0:
                irasas.pavadinimas = pavadinimas
            if len(tipas) > 0:
                irasas.tipas = tipas
            if len(aljansas) > 0:
                irasas.aljansas = aljansas
            if len(korporacija) > 0:
                irasas.korporacija = korporacija
            session.commit()
            print(f"Naujas irasas {irasas} atnaujintas sekmingai.")

def trynimas():
    pasalinti = ivedimas_stociu()
    if pasalinti:
        session.delete(pasalinti)
        session.commit()
        print(f"Irasas {pasalinti} pasalintas sekmingai")

while True:
    print("___Stociu duonbaze___")
    print("Pasirinkite: ")
    print("- z: iseiti.")
    print("- v: rodyti visas stotis.")
    print("- r: naujas regionas.")
    print("- s: nauja stotis.")
    print("- p: pakeisti stoties duomenis.")
    print("- t: trinti stoti.")
    print("- o: naujas puolejas.")
    print("- d: naujas dalyvis.")
    print("- l: laikas.")
    pasirinkimas = input("Pasirinkite: ").casefold()
    if pasirinkimas == "z":
        print("ARGH.... varom vogti!")
        break
    if pasirinkimas == "v":
        stociu_lentele()
    if pasirinkimas == "r":
        naujas_regionas()
    if pasirinkimas == "s":
        nauja_stotis()
    if pasirinkimas == "p":
        atnaujinti_stotis()
    if pasirinkimas == "t":
        trynimas()
    if pasirinkimas == "o":
        naujas_puolejas()
    if pasirinkimas == "d":
        naujas_dalyvis()
    if pasirinkimas == "l":
        naujas_data()
    else:
        print(">>>> Pasirink is Naujo >>>>")
