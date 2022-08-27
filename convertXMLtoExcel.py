import xml.etree.ElementTree as ETree
import pandas as pd
Tree = ETree.parse("http://cdn.salontracker.co.uk/publicwebdownloads/HelpVideos/HelpVideoConfig.xml")# input file
root = Tree.getroot()
A= []
for ele in root:
    B = {}
    for i in list(ele):
        B.update({i.tag: i.text})
        A.append(B)
df = pd.DataFrame(A)
df.drop_duplicates(keep = 'first', inplace = True)
df.reset_index(drop=True, inplace = True)
writer = pd.ExcelWriter("B:/Output354.xlsx", engine = 'xlsxwriter')
df.to_excel(writer,sheet_name='sheet1')
worksheet= writer.sheets['sheet1']
worksheet.set_column('B:Z',30)
writer.save()
print('xml to Excel conversion successful')
excel_file_path = "B:/Output354.xlsx"
df = pd.read_excel(excel_file_path)
#print(df.head(2))
for column in df.columns:
    df[column]= df[column].astype(str).str.replace(r'\W',"")
df.to_excel("B:Clean_data.xlsx")