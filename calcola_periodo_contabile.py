from datetime import date, timedelta
import calendar

def get_accounting_dates(today=None):
    today = today or date.today()
    
    # Calcola in quanti giorni finisce il mese
    last_day_of_month = date(today.year, today.month, calendar.monthrange(today.year, today.month)[1])
    days_to_month_end = (last_day_of_month - today).days

    # Calcolo periodo attuale
    if days_to_month_end < 7:
        # Se siamo negli ultimi 6 giorni del mese
        apertura = today - timedelta(days=today.weekday())  # Lunedì della settimana attuale
        chiusura = last_day_of_month
    else:
        apertura = today - timedelta(days=today.weekday())  # Lunedì della settimana attuale
        chiusura = apertura + timedelta(days=6)  # Domenica della stessa settimana
        # Se la domenica è di un altro mese, accorcia il periodo a fine mese
        if chiusura.month != apertura.month:
            chiusura = last_day_of_month

    # Prossimo periodo contabile
    next_month = today.replace(day=28) + timedelta(days=4)  # Vai al prossimo mese in modo robusto
    first_day_next_month = next_month.replace(day=1)
    # Calcola la prima domenica del mese successivo
    days_to_sunday = (6 - first_day_next_month.weekday()) % 7
    prossima_chiusura = first_day_next_month + timedelta(days=days_to_sunday)
    prossima_apertura = first_day_next_month

    return apertura, chiusura, prossima_apertura, prossima_chiusura

# Esempio di utilizzo
apertura, chiusura, prossima_apertura, prossima_chiusura = get_accounting_dates()
print("📅 Apertura periodo attuale:", apertura)
print("📅 Chiusura periodo attuale:", chiusura)
print("📅 Prossima apertura:", prossima_apertura)
print("📅 Prossima chiusura:", prossima_chiusura)
