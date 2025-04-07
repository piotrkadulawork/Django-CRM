# Django CRM (DCRM)

To prosty projekt CRM (Customer Relationship Management) stworzony w Django jako część nauki frameworka.

Pozwala na zarządzanie bazą klientów – dodawanie, edytowanie, przeglądanie i usuwanie rekordów.

## 🎥 Tutorial

Projekt powstał na podstawie materiału wideo dostępnego na YouTube:

👉 [Zobacz tutorial na YouTube](https://www.youtube.com/watch?v=t10QcFx7d5k&t=5416s)

## 🛠️ Technologie

- Python 3
- Django
- HTML / CSS (Bootstrap)
- MySql

## 🚀 Jak uruchomić projekt

```bash
git clone https://github.com/piotrkadulawork/Django-CRM
cd dcrm
python -m venv virt
source virt/bin/activate  # Windows: virt\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver