# Analiza Projekta MrSnowman

## Informacije o Autoru

- **Ime i Prezime:** Tamara Savić
- **Broj Indeksa:** 1057/2021

## Opis Projekta

MrSnowman je C++ Qt projekat koji predstavlja 2D igru u kojoj pomažete snešku na njegovom opasnom putovanju!

- **Izvorni Kod Projekta:** [MrSnowman](https://gitlab.com/matf-bg-ac-rs/course-rs/projects-2021-2022/04-MrSnowman)
- **Analizirana Grana:** master
- **Hash Commit-a:** f28a6c201c1a70c35364b434ad601bb352846205

## Alati za Analizu

Za analizu projekta korišćeno je pet alata:

1. **Address Sanitizer (ASan):**
    - Dinamička analiza
    - Detekcija memorijskih problema

2. **Astyle:**
    - Formatiranje koda

3. **Clang Static Analyzer:**
    - Statička analiza
    - Detekcija potencijalnih grešaka u kodu

4. **Thread Sanitizer (TSan):**
    - Dinamička analiza
    - Detekcija problema sa nitima

5. **Unit Testovi:**
    - Dinamička analiza
    - Detekcija grešaka i pokrivenosti koda

### Uputstva za Reprodukciju Rezultata

Pre pokretanja skripti, inicijalizujte submodul projekta koristeći sledeću komandu:

```bash
git submodule update --init --recursive --checkout
```

Za pokretanje analize, koristite odgovarajuće skripte koje se nalaze u odgovarajućim direktorijumima za svaki alat:

- **Address Sanitizer:** `./run_asan.sh` (nalazi se u direktorijumu za Address Sanitizer)
- **Astyle:** `./run_astyle.sh` (nalazi se u direktorijumu za Astyle)
- **Clang Static Analyzer:** `./run_clang.sh` (nalazi se u direktorijumu za Clang Static Analyzer)
- **Thread Sanitizer:** `./run_tsan.sh` (nalazi se u direktorijumu za Thread Sanitizer)
- **Unit Testovi:** `./run_tests.py` (nalazi se u direktorijumu za Unit Testove)


### Zaključci

- **Address Sanitizer:** Nema detektovanih grešaka ili upozorenja.
- **Thread Sanitizer:** Nema detektovanih grešaka ili upozorenja.
- **Astyle:** Formatiranje koda je uspešno primenjeno na određene fajlove.
- **Clang Static Analyzer:** Nisu pronađene greške ili upozorenja.
- **Unit Testovi:** Pokrivenost koda i funkcionalnosti je analizirana i dostupna u `coverage-html` folderu.

### Napomena

Informacije o korišćenju alata se nalaze u odgovarajućim README.md fajlovima unutar foldera za svaki alat.

