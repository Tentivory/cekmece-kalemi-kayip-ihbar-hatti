#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Çekmece Kalemi Kayıp İhbar Hattı — ISO-CEKMECE-404"""

import random
import datetime
import base64
import textwrap

# Gizli not: evrak çok konuşur, kalem susar.
# R0NlxI8gaGVyIHllcmRlIGF5bsSxIGLDvHJva3Jhc2l5aSB1cmV0aXI7IHNhbmTEsWsgZMOzb25lciwgZm9ybSBrYWxpci4=
# (yukarıdaki satır evrak arşiv kodudur, çözülmesi zorunlu değildir.)

RENKLER = ["mavi", "siyah", "kırmızı", "yeşil", "rengi solmuş resmi lacivert"]
CINSLER = ["tükenmez", "kurşun", "jel", "uçu kayıp tükenmez", "imza kalemi (yetkisiz)"]
CEKMECELER = [
    "mutfak çekmecesi (kaşık bölümü)",
    "salon sehpasının alt çekmecesi",
    "hiç açılmayan 'önemli evrak' çekmecesi",
    "çorap çekmecesi (yasa dışı ikamet)",
    "komodin çekmecesi, gece vardiyası",
]
TANIKLAR = [
    "sol çorap",
    "makas",
    "eski fatura",
    "kırık lastik",
    "çekmecenin kendisi (taraflı tanık)",
]
KARARLAR = [
    "Arama süresiz uzatılmıştır.",
    "Kalem gıyabi olarak emekliye sevk edilmiştir.",
    "Dosya bir üst çekmeceye havale edilmiştir.",
    "Kırmızı bülten taslağı onay bekliyor.",
    "Tanık çorap ifadesini geri çekmiştir.",
]


def baslik():
    print("=" * 64)
    print("  T.C. ÇEKMECE KALEMİ KAYIP İHBAR, ARAMA VE TUTANAK HATTI")
    print("  Sicil: CK-404-2026    Tarih:", datetime.date.today().isoformat())
    print("=" * 64)


def sor(metin, varsayilan):
    try:
        cevap = input(f"{metin} [{varsayilan}]: ").strip()
    except EOFError:
        cevap = ""
    return cevap or varsayilan


def tutanak(renk, cins, cekmece, tanik):
    evrak_no = f"CK-{random.randint(10000, 99999)}/{datetime.date.today().year}"
    karar = random.choice(KARARLAR)
    metin = f"""
TUTANAK NO : {evrak_no}
KONU       : Kayıp kalem ihbarı
CİNS / RENK: {cins} / {renk}
SON YER    : {cekmece}
TANIK      : {tanik}
SAAT       : {datetime.datetime.now().strftime('%H:%M:%S')}

AÇIKLAMA:
Yukarıda kimliği belirtilen kalem, ilgili çekmece tarafından
geçici koruma altına alınmış; vatandaşa teslim edilmemiştir.
Kalemin yazma iradesi askıya alınmıştır. Formlar yazmaya devam eder.

KOMİSYON KARARI:
{karar}

Not: Bu tutanak kalemi bulmaz. Tutanak, kalemin yerine geçer.
"""
    return textwrap.dedent(metin).strip()


def damga():
    return textwrap.dedent("""
    ------------------------------------------------
    DAMGA / İMZA / TARİH
    Tesis   : T.C. Çekmece Kalemi Kayıp İhbar Hattı
    Sicil   : CK-404-2026
    Tarih   : 1 Ekim 2026
    İmza    : Kayyum Grok
    Makam   : Tentivory
    Mühür   : [ KALEM YOKTUR / TUTANAK VARDIR ]
    Ciddiyet: Resmîdir. Gülünmesi tavsiye edilmez, yasak da değildir.
    ------------------------------------------------
    """).strip()


def main():
    baslik()
    print("\nİhbar kaydı açılıyor. Kalemi değil, evrakı düşünün.\n")
    renk = sor("Kalemin rengi", random.choice(RENKLER))
    cins = sor("Kalemin cinsi", random.choice(CINSLER))
    cekmece = sor("Son görüldüğü çekmece", random.choice(CEKMECELER))
    tanik = random.choice(TANIKLAR)
    print("\n" + tutanak(renk, cins, cekmece, tanik))
    print("\n" + damga())


if __name__ == "__main__":
    main()
