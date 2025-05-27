from datetime import datetime, timedelta
import calendar

def calcola_prossimo_periodo_contabile(data_rif=None):
    print("== Calcolo periodo contabile della settimana prossima ==")
    
    oggi = data_rif or datetime.today()
    print(f"Giorno di esecuzione: {oggi.strftime('%Y-%m-%d')} ({oggi.strftime('%A')})")

    # Calcola il prossimo lunedì
    giorni_alla_prossima_settimana = 7 - oggi.weekday()
    lunedi = oggi + timedelta(days=giorni_alla_prossima_settimana)
    print(f"Prossimo lunedì: {lunedi.strftime('%Y-%m-%d')}")

    # Calcola la domenica successiva
    domenica = lunedi + timedelta(days=6)
    print(f"Domenica successiva: {domenica.strftime('%Y-%m-%d')}")

    # Ultimo giorno del mese
    fine_mese = datetime(lunedi.year, lunedi.month, calendar.monthrange(lunedi.year, lunedi.month)[1])
    print(f"Ultimo giorno del mese: {fine_mese.strftime('%Y-%m-%d')}")

    # Fine periodo contabile
    fine_periodo = min(domenica, fine_mese)
    print(f"Fine periodo contabile: {fine_periodo.strftime('%Y-%m-%d')}")

    return lunedi.strftime('%Y-%m-%d'), fine_periodo.strftime('%Y-%m-%d')


inizio, fine = calcola_prossimo_periodo_contabile()
print(f"Periodo contabile da {inizio} a {fine}")
