import csv

def read_csv(path):
  # funcion abrir el erchivo CSV
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # nombre de las columnas se encuntran en la primera fila
    header = next(reader)
    data = []
    # se hace el recorrido de las filas
    for row in reader:
      iterable = zip(header, row)
      # une los valores de las listas en tuplas
      country_dict = { key: value for key, value in iterable}
      data.append(country_dict)
    return data

# correr el archivo como script desde la terminal
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])