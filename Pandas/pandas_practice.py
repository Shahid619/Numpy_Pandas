# Load products.csv → show first 10 rows.

import pandas as pd
df=pd.read_csv('data.csv')
# print(df.to_string())


# ========================================
# Select and print : only Pulse category.

# print('\n Pulse data only : ',df['Pulse'])


# ==========================================
# Filter rows with Maxpulse > 140.

maxpulse=[]
for i in df['Maxpulse']:
    if i>140:
        maxpulse.append(i)

# maxpulse=pd.DataFrame(maxpulse) #--optional--
# print(f'\nMaxPulse > 140 : {maxpulse}')


# =====================
# Drop rows with missing values.

mean_cal=df['Calories'].mean()
new_df=df.fillna({'Calories':mean_cal})
# print(new_df.to_string())


# ========================
# Add a new column “Total = Quantity * Price”.

new_df['Pulse*Calories'] =new_df['Pulse']*new_df['Calories']
# print(df.head(10))

# print(new_df.to_string())


# ===============================
# drop duplicates
new_df.drop_duplicates(inplace=True)

# ===================================
# correct the Duration colmn ,as there are few outliers.

for i in new_df.index:
    if new_df.loc[i,'Duration'] > 60:
        new_df.loc[i,'Duration']=60

    elif new_df.loc[i,'Duration']<30:
        new_df.loc[i,'Duration']=30
# print(new_df.to_string())
# print(new_df.head())


# =============================================
# Bin duration into : less , Normal , high .

bin=[0,31,46,70]
labels=['less_workout','Normal_workout','high_workout']

Duration_label=pd.cut(
    df['Duration'],
    bins=bin,
    labels=labels,
    right=False
)
print(new_df.head())
print(Duration_label.head())
print(Duration_label.value_counts())