import pandas as pd


file1 = pd.DataFrame({
    'Mobile': ['9990000001', '9990000002',],
    'Site': ['SiteA', 'SiteB']
})
file1.to_csv('file1.csv', index=False)


file2 = pd.DataFrame({
    'Mobile': ['9990000001', '9990000003'],
    'PortOutDate': ['2024-01-10', '2024-02-15'],
    'PortOutOperator': ['Airtel', 'Jio']
})
file2.to_csv('file2.csv', index=False)


file3 = pd.DataFrame({
    'Mobile': ['9990000001', '9990000002'],
    'Retailer': ['R1', 'R2'],
    'PortInDate': ['2024-01-20', '2024-03-10'],
    'DonorOperator': ['Airtel', 'Vi']
})
file3.to_csv('file3.csv', index=False)


file4 = pd.DataFrame({
    'Retailer': ['R1', 'R2',],
    'Site': ['SiteA', 'SiteB',],
    'TerritoryManager': ['TM1', 'TM2', ]
})
file4.to_csv('file4.csv', index=False)



f1 = pd.read_csv('file1.csv')
f2 = pd.read_csv('file2.csv')
f3 = pd.read_csv('file3.csv')
f4 = pd.read_csv('file4.csv')



port_in = f3.merge(f1, on='Mobile', how='left') \
            .merge(f4, on=['Retailer', 'Site'], how='left')


port_out = f2.merge(f1, on='Mobile', how='left') \
             .merge(f4, on='Site', how='left')


port_in_count = port_in.groupby('TerritoryManager')['Mobile'].count().rename('PortInCount')
port_out_count = port_out.groupby('TerritoryManager')['Mobile'].count().rename('PortOutCount')


summary = pd.concat([port_in_count, port_out_count], axis=1).fillna(0)
summary['PortIn/PortOut Ratio'] = summary['PortInCount'] / summary['PortOutCount'].replace(0, 1)


print("Territory Manager Wise Porting Summary:\n")
print(summary)
