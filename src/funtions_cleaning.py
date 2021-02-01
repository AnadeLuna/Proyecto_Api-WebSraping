"Libraries that i will need to use"
import numpy as np
import pandas as pd

'''This funtion is going to clean all the DataSet. And it´s going to return 
the unemployment of the different communities in Spain during the months of 2020.'''
    
def clean_dataset():
    
    "1ºFuntion to introduce the path."
    path = input("Introduce the path of the file : ")

    "2ºFuntion to import and read the CSV file."
    data = pd.read_csv(path,encoding = "ISO-8859-1")
    
    "3º Check the DataSet."
    print(data.shape)
    print(data.columns)
    print(data.head(3))

    "4º Remove all the duplicate data."
    data = data.drop_duplicates()

    "5º Remove columns: Codigo Provincia,Provincia,Codigo Municipio,Municipio"
    data.drop(columns = ["Codigo Provincia","Provincia","Codigo Municipio"," Municipio"])

    "6º Check the columns through which i want to filter."
    print(" Total Comunidades Autónomas :",len(data["Comunidad Autónoma"].unique()))
    print(" Total months :",len(data["mes"].unique()))

    "7º Funtion to group by `mes` and `Comunidad Autónoma`."
    data = data.groupby(['mes','Comunidad Autónoma'])['total Paro Registrado', 'Paro hombre edad < 25',
    'Paro hombre edad 25 -45 ', 'Paro hombre edad >=45',
    'Paro mujer edad < 25', 'Paro mujer edad 25 -45 ',
    'Paro mujer edad >=45', 'Paro Agricultura', 'Paro Industria',
    'Paro Construcción', 'Paro Servicios', 'Paro Sin empleo Anterior'].sum()
    print(data[:19])
    
    "8º Funtion to eliminate de null values."
    data = data.reset_index()

    "9º Funtion to eliminate de null values."
    print(data.isnull().values.any())

    "10º Change the names of the `mes`."
    print(data["mes"].unique())
    data["mes"][data["mes"] == 'Abril de 2020'] = "Apr"
    data["mes"][data["mes"] == 'Agosto de 2020'] = "Aug"
    data["mes"][data["mes"] == 'Enero de 2020'] = "Jan"
    data["mes"][data["mes"] == 'Febrero de 2020'] = "Feb"
    data["mes"][data["mes"] == 'Julio de 2020'] = "Jul"
    data["mes"][data["mes"] == 'Junio de 2020'] = "Jun"
    data["mes"][data["mes"] == 'Marzo de 2020'] = " Mar"
    data["mes"][data["mes"] == 'Mayo de 2020'] = "May"
    data["mes"][data["mes"] == 'Noviembre de 2020'] = "Nov"
    data["mes"][data["mes"] == 'Octubre de 2020'] = "Oct"
    data["mes"][data["mes"] == 'Septiembre de 2020'] = "Sep"


    "11º Change the names of the `Comunidad Autónoma`."
    print(data["Comunidad Autónoma"].unique())
    data["Comunidad Autónoma"][data["Comunidad Autónoma"] == 'Asturias; Principado de'] = 'Principado de Asturias'
    data["Comunidad Autónoma"][data["Comunidad Autónoma"] == 'Balears; Illes'] = 'Islas Baleares'
    data["Comunidad Autónoma"][data["Comunidad Autónoma"] == 'Castilla - La Mancha'] = 'Castilla-La Mancha'
    data["Comunidad Autónoma"][data["Comunidad Autónoma"] == 'Comunitat Valenciana'] = 'Comunidad Valenciana'
    data["Comunidad Autónoma"][data["Comunidad Autónoma"] == 'Madrid; Comunidad de'] = 'Comunidad de Madrid'
    data["Comunidad Autónoma"][data["Comunidad Autónoma"] == 'Murcia; Región de'] = 'Región de Murcia'
    data["Comunidad Autónoma"][data["Comunidad Autónoma"] == 'Navarra; Comunidad Foral de'] = 'Navarra'
    data["Comunidad Autónoma"][data["Comunidad Autónoma"] == 'Rioja; La'] = 'La Rioja'                 

    "12º Change the name of the columns."
    print(data.columns)
    data= data.rename(columns={'mes':'Month','total Paro Registrado':'Total Paro Registrado','Paro hombre edad < 25':'Hombre edad < 25','Paro hombre edad 25 -45 ':'Hombre edad 25-45','Paro hombre edad >=45':'Hombre edad >=45','Paro mujer edad < 25':'Mujer edad < 25','Paro mujer edad 25 -45 ':'Mujer edad 25-45','Paro mujer edad >=45':'Mujer edad >= 45'})
    
    "13º Export the DataSet to a .csv file."
    data.to_csv("data_clean.csv",index=False)