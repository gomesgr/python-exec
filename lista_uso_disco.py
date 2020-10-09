import pandas as pd

def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    power_labels = {0: '', 1: 'k', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        if n == 2: return size, power_labels[n]+'B'
        size /= power
        n += 1
    return size, power_labels[n]+'B'

csv = pd.read_csv('lista.csv')
data = pd.DataFrame(csv)
data_renamed = data.rename(columns={'nomes': 'usuario', 'uso_disco': 'espaco_utilizado'})
new_data = []
for data in data_renamed.itertuples():
    new_data.append(data.espaco_utilizado)
print('New data ', new_data)
data_renamed['espaco_utilizado'].replace(
    {size: f'{format_bytes(size)[0]:.2f}' for size in new_data},
    inplace=True)
values_sum = sum([format_bytes(size)[0] for size in new_data])
values_sum = float(f'{values_sum:.2f}')
# v * 100 / tot
data_renamed.insert(2, '%_de_uso',
                    [float(data.espaco_utilizado) * 100 / values_sum
                     for data in data_renamed.itertuples()])
print(sum([data._3 for data in data_renamed.itertuples()]))
print(data_renamed)
