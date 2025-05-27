from datetime import date, timedelta, datetime
import calendar

def get_accounting_dates(today=None):
    today = today or date.today()

    # Calcola apertura e chiusura candidati (settimana contabile corrente)
    apertura = today - timedelta(days=today.weekday())  # lunedì corrente
    chiusura_candidata = apertura + timedelta(days=6)   # domenica

    # Fine mese del mese di apertura
    last_day_of_month = date(apertura.year, apertura.month, calendar.monthrange(apertura.year, apertura.month)[1])
    days_from_apertura_to_month_end = (last_day_of_month - apertura).days

    # === PERIODO ATTUALE ===
    if days_from_apertura_to_month_end < 7 or chiusura_candidata.month != apertura.month:
        chiusura = last_day_of_month
    else:
        chiusura = chiusura_candidata

    # === PROSSIMO PERIODO ===
    giorno_successivo = chiusura + timedelta(days=1)

    if giorno_successivo.weekday() == 6:
        # Se il giorno dopo è domenica, periodo = 1 solo giorno
        prossima_apertura = giorno_successivo
        prossima_chiusura = giorno_successivo
    else:
        days_to_sunday = (6 - giorno_successivo.weekday()) % 7
        prossima_apertura = giorno_successivo
        prossima_chiusura = giorno_successivo + timedelta(days=days_to_sunday)

    return apertura, chiusura, prossima_apertura, prossima_chiusura

# === INPUT MANUALE ===
input_str = input("Inserisci una data (YYYY-MM-DD): ").strip()
try:
    test_date = datetime.strptime(input_str, "%Y-%m-%d").date()
except ValueError:
    print("Formato non valido. Uso la data di oggi.")
    test_date = None

apertura, chiusura, prossima_apertura, prossima_chiusura = get_accounting_dates(test_date)

print("📅 Apertura periodo attuale:", apertura)
print("📅 Chiusura periodo attuale:", chiusura)
print("📅 Prossima apertura:", prossima_apertura)
print("📅 Prossima chiusura:", prossima_chiusura)
