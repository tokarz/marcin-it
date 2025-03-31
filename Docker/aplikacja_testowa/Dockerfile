# Pobieramy oficjalny obraz Pythona
FROM python:3.10

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy wszystkie pliki z lokalnego katalogu do kontenera
COPY . .

# Instalujemy zależności
RUN pip install -r requirements.txt

# Uruchamiamy aplikację
CMD ["python", "app.py"]