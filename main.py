
earth_acceleration = 9.81



def berechne_gewichtskraft(start_kg, end_kg, erdbeschleunigung=9.81):
    # Überprüfen, ob der Endwert größer als der Anfangswert ist
    if start_kg > end_kg:
        print("Der Endwert muss größer oder gleich dem Anfangswert sein.")
        return

    # Erstellen einer Liste von Massen mit einem Schritt von 0,5 kg
    massen = [round(m, 1) for m in list(frange(start_kg, end_kg, 0.5))]

    # Berechnen der Gewichtskräfte (F = m * g)
    gewichtskraefte = [masse * erdbeschleunigung for masse in massen]


    for masse, kraft in zip(massen, gewichtskraefte):
        print(f"Masse: {masse} kg - Gewichtskraft: {kraft:.2f} N")


# Hilfsfunktion Schritte erstellen
def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step



berechne_gewichtskraft(2.5, 630)
