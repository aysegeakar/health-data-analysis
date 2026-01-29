import pandas as pd
import matplotlib.pyplot as plt

# Veri
data = {
    'PatientID': [1,2,3,4,5],
    'Age': [25, 34, 28, 52, 46],
    'Cholesterol': [180, 220, 190, 240, 200]
}
df = pd.DataFrame(data)

# Basit analiz
print("Ortalama yaş:", df['Age'].mean())
print("Ortalama kolesterol:", df['Cholesterol'].mean())

# Grafik oluştur
plt.scatter(df['Age'], df['Cholesterol'], color='blue')
plt.title('Age vs Cholesterol')
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.savefig('age_vs_cholesterol.png')  # görseli kaydet
plt.show()
