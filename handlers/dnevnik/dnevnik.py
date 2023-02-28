from pydnevnikruapi.dnevnik import dnevnik

def get_dnevnik(login, password):
    dn = dnevnik.DiaryAPI(login=login, password=password)
    return dn