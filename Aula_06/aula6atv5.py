
"""
email = input("Digite seu email:")
jogajunto = "@jogajuntoinstituto.org"

for verifica_email_jj in jogajunto:
     if verifica_email_jj in jogajunto:
        print(f"O e-mail {email} contém {jogajunto}")
else:
     print(f"O E-mail {email} não contém {jogajunto}")

"""
verifica_email_jj = False
dominio = "jogajuntoinstituto.org"

while verifica_email_jj == False:
    email = input("Digite seu email:")

    if dominio in email:
        print(f"O e-mail {email} contém {dominio}")
        email = True
    else:
        print(f"esse e-mail {email} não contém {dominio}")

