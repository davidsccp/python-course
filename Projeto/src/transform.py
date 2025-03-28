import pandas as pd

def calc_horas(coluna_tempo_voo):
    """Converte minutos para horas, com uma casa decimal."""
    return coluna_tempo_voo / 60.0

def classifica_turno(coluna_data_hora):
    """Classifica o turno do dia baseado no horário."""
    horarios = pd.to_datetime(coluna_data_hora).dt.hour

    def get_turno(h):
        if 6 <= h < 12:
            return 'MANHÃ'
        elif 12 <= h < 18:
            return 'TARDE'
        elif 18 <= h < 24:
            return 'NOITE'
        else:
            return 'MADRUGADA'

    return horarios.apply(get_turno)
