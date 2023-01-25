import csv
import datetime

nif_dict = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M", "6": "Y", "7": "F", "8": "P",
                            "9": "D",
                            "10": "X", "11": "B", "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
                            "18": "H",
                            "19": "L", "20": "C", "21": "K", "22": "E"}



def check_username(nom):
    """Esta funcion devuelve una cadena con la primera letra de cada palabra en mayuscula.
            PARAMTROS:
                    -nom: Nombre en minusculas que tenemos que pasar las primeras letras.
            Salida: Nombre con la primera letra en mayuscula."""

    return nom.title()

def check_nif(dni):
    """Esta funcion corrige la letra del DNI introducido realizando el resto de todos los numeros del DNI entre 23
    PARAMETROS:
                dni= Es el dni introducido por el usuario, después se corregirá
                resto= resultado del cociente
                final= la letra correspondiente a ese cociente"""
    dni_sin_letra = dni[0:8]
    resto = int(dni_sin_letra) % 23
    final = dni_sin_letra + nif_dict[str(resto)]
    return str(final)




def check_DGT(ruta):
    """Esta funcion recoje un excel con diferentes parametros y reesctibe todos ellos corrigiendo los diferentes
    parametros y reorganizando las celdas.
    PARAMETROS:
                ruta= Nombre del archivo el cual queremos modificar.
    Salida: se creará un archivo en la carpeta que tenga guardado esta función, el cual tendrá todos los datos corregidos.
    """

    with open(ruta, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)


        csv_out = []

        for persona in reader:
            if persona[0] != "Nombre":

                name = persona[0]
                dni = persona[1]


                csv_out.append([check_username(name), check_nif(dni)])

        excel_escritor = csv.writer(csvfile)

    with open(ruta, encoding="utf-8") as salida:
        csvsalida = open('salida.csv', 'w', newline='')
        salida = csv.writer(csvsalida,
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for linea in csv_out:
            salida.writerow(linea)
    return

start_time = datetime.datetime.now()
ruta = input("Introduce en nombre de tu archivo")
check_DGT(ruta)
end_time = datetime.datetime.now()
print(end_time - start_time)