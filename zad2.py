'''
Program do weryfikacji unikalności nazwy Użytkownika:

proszę utworzyć listę current_users, o co najmniej dwóch elementach zawierających przykładowe loginy istniejących Użytkowników (0.5 pkt),

proszę utworzyć listę new_users, o co najmniej dwóch elementach zawierających przykładowe loginy nowych Użytkowników, gdzie co najmniej jeden login występuje również na liście current_users (0.5 pkt),

proszę zweryfikować za pomocą iteracji i instrukcji warunkowej czy któraś z nazw Użytkowników na liście new_users została już wykorzystana w systemie, w ramach listy current_users (2 pkt),

proszę powtórzyć weryfikację z dodatkowym założeniem, iż wielkość liter w nazwie Użytkownika nie ma znaczenia przy porównaniu (3.5 pkt).
'''

current_users = ["piotrek12", "jacek45", "BogDanKL"]
new_users = ["piotrek12", "kasia99", "bOGdANkl"]

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print(f"The user: '{new_user}' already exists")
    else:
        print(f"Allowed username: {new_user}")
