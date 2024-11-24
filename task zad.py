#TASK 1

# Alış-Veriş Endirimi Hesablayıcı
#def endirim_hesabla():
#    try:
        # İstifadəçidən məbləği daxil etməsini istəyirik
#        mebleg = float(input("Alış-veriş məbləğini daxil edin (AZN): "))
        
#        if mebleg > 300:
#            endirim = mebleg * 0.10  # 10% endirim
#        elif mebleg > 100:
#            endirim = mebleg * 0.05  # 5% endirim
#        else:
#            endirim = 0  # Endirim yoxdur

#        yekun_mebleg = mebleg - endirim

        # Nəticələri göstəririk
#        print(f"\nAlış-veriş məbləği: {mebleg:.2f} AZN")
#        print(f"Endirim: {endirim:.2f} AZN")
#        print(f"Yekun məbləğ: {yekun_mebleg:.2f} AZN")
#    except ValueError:
#        print("Zəhmət olmasa düzgün rəqəm daxil edin.")

# Proqramı işə salırıq
#endirim_hesabla()


#TASK 2

# # Vergi Kalkulyatoru
# def vergi_kalkulyatoru():
#     try:
#         # İstifadəçidən illik gəliri daxil etməsini istəyirik
#         gelir = float(input("İllik gəlirinizi daxil edin (AZN): "))
        
#         # Vergi hesablaması
#         if gelir <= 20000:
#             vergi = gelir * 0.05  # 5% vergi
#         elif gelir <= 50000:
#             vergi = gelir * 0.10  # 10% vergi
#         else:
#             vergi = gelir * 0.15  # 15% vergi
        
#         net_gelir = gelir - vergi  # Vergi sonrası gəlir

#         # Nəticələri göstəririk
#         print(f"\nİllik gəlir: {gelir:.2f} AZN")
#         print(f"Hesablanan vergi: {vergi:.2f} AZN")
#         print(f"Vergi sonrası gəlir: {net_gelir:.2f} AZN")
#     except ValueError:
#         print("Zəhmət olmasa düzgün rəqəm daxil edin.")

# # Proqramı işə salırıq
# vergi_kalkulyatoru()

# TASK 3

# Risk Qiymətləndirmə Sistemi
# def risk_qiymetlendirme():
#     try:
#         # İstifadəçidən təzyiq və şəkər səviyyəsini daxil etməsini istəyirik
#         tezyiq = int(input("Təzyiq səviyyəsini daxil edin: "))
#         seker = int(input("Şəkər səviyyəsini daxil edin: "))
        
#         # Risk səviyyəsinin qiymətləndirilməsi
#         if tezyiq > 140 and seker > 120:
#             risk_seviyesi = "Yüksək risk — Həkimə müraciət edin."
#         elif tezyiq > 130 and seker > 100:
#             risk_seviyesi = "Orta risk — Müntəzəm yoxlama tövsiyə olunur."
#         else:
#             risk_seviyesi = "Aşağı risk — Sağlamlıq vəziyyətiniz normaldır."

#         # Nəticəni göstəririk
#         print(f"\nNəticə: {risk_seviyesi}")
#     except ValueError:
#         print("Zəhmət olmasa düzgün rəqəmlər daxil edin.")

# # Proqramı işə salırıq
# risk_qiymetlendirme()
