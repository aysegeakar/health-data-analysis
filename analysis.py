# analysis.py
import pandas as pd

# Örnek veri (CSV yerine kendi veri setini koyabilirsin)
data = {
    'PatientID': [1,2,3,4,5],
    'Age': [25, 34, 28, 52, 46],
    'Cholesterol': [180, 220, 190, 240, 200]
}

df = pd.DataFrame(data)

# Basit analiz
print("Ortalama yaş:", df['Age'].mean())
print("Ortalama kolesterol:", df['Cholesterol'].mean())
