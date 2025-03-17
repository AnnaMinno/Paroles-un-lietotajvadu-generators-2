import names
import random

print("\n Randoma lietotājvārda un paroles ģenerātors. ")
print("\n Vispirms izdomāsīm Lietotājvārdu. ")
while True:
    print(
        "\nLūdzu izvelēties sava dzimuma burtu: V (vīriešu) vai S (sieviešu)")
    burts = input()
    try:
        if burts == "V":
            for i in range(1):
                v_vards = names.get_full_name(gender="male")
                v_vards_2 = v_vards.split()
                v_varda_1burts = v_vards_2[0][0]
                v_uzvards_burti = v_vards_2[-1]
                v_cipars = '{:03d}'.format(random.randrange(1, 999))
                v_lietotaj_vards = (v_varda_1burts + v_uzvards_burti +
                                    v_cipars)
            print(f'Jūsu lietotājvārds ir {v_lietotaj_vards}')
        elif burts == "S":
            for i in range(1):
                s_vards = names.get_full_name(gender="female")
                s_vards_2 = s_vards.split()
                s_varda_1burts = s_vards_2[0][0]
                s_uzvards_burti = s_vards_2[-1]
                s_cipars = '{:03d}'.format(random.randrange(1, 999))
                s_lietotaj_vards = (s_varda_1burts + s_uzvards_burti +
                                    s_cipars)
            print(f'Jūsu lietotājvārds ir {s_lietotaj_vards}')
        else:
            print("Ievadiet vai burtu V vai burtu S!")
            continue
    except:
        print("Ievadiet vai burtu V vai burtu S!")
        continue
    break

print("\n Tagad izdomāsīm paroli. ")
m_burti = "abcdefghijklmnopqrstuvwxyz"
l_burti = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipari = "1234567890"
garums = int(input("Ievadiet cik garu paroli Jūs gribāt:"))
paroles_dalas = m_burti + l_burti + cipari
parole = "".join(random.sample(paroles_dalas, garums))
print(f'Jūsu parole ir {parole}')