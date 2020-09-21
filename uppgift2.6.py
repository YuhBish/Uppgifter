svar = int(input("Skriv ett antal sekunder: "))
sek = int(svar)

år =  sek // 31556926
sek = sek % 31556926
mån = sek // 2629744
sek = sek % 2629744
vck = sek // 604800
sek = sek % 604800
dag = sek // 86400
sek = sek % 86400
tim = sek // 3600
sek = sek % 3600
min = sek // 60
sek = sek % 60


print("År", år)
print("Månad", mån)
print("Veckor", vck)
print("Dagar", dag)
print("Timmar", tim)
print("Minuter", min)
print("Sekunder", sek)