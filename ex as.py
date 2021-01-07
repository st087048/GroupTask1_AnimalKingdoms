import csv


Bacteria = []
Archaea = []
Protista = []
Chromista = []
Plants = []
Animals = []
Fungi = []
Viruses = []


type_of_diet = []
cyst_formation = []
chitin = []
core_alability = []
presence_of_pseudomurein = []
eterna_growth = []
chlorophyll_type = []


# Чтение csv файла и рассортировка данных
with open('animals - Лист1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        type_of_diet.append(row['type_of_diet'])
        cyst_formation.append(int(row['cyst_formation']))
        chitin.append(int(row['chitin']))
        core_alability.append(int(row['core_alability']))
        presence_of_pseudomurein.append(int(row['presence_of_pseudomurein']))
        eterna_growth.append(int(row['eterna_growth']))
        chlorophyll_type.append(row['chlorophyll_type'])


for obj in range(len(chitin)):
    if(type_of_diet[obj] == '-'):
        Viruses.append(obj)
    elif(type_of_diet[obj] == 'A'):
        if(core_alability[obj] == 0):
            if(presence_of_pseudomurein[obj] == 1):
                Archaea.append(obj)
            else:
                Bacteria.append(obj)
        else:
            if(cyst_formation[obj] == 1):
                Protista.append(obj)
            elif(eterna_growth[obj] == 1):
                Plants.append(obj)
            else:
                Chromista.append(obj)
    else:
        if(cyst_formation[obj] == 1):
            if(core_alability[obj] == 1):
                Protista.append(obj)
            else:
                Bacteria.append(obj)
        else:
            if(eterna_growth[obj] == 1):
                Fungi.append(obj)
            else:
                if(chlorophyll_type[obj] == '-'):
                    Animals.append(obj)
                else:
                    Chromista.append(obj)


print('Bacteria', Bacteria)
print('Archaea', Archaea)
print('Protista', Protista)
print('Chromista', Chromista)
print('Plants', Plants)
print('Animals', Animals)
print('Fungi', Fungi)
print('Viruses', Viruses)
#print(len(Viruses) + len(Bacteria) + len(Archaea) + len(Protista)
#      + len(Chromista) + len(Animals) + len(Plants) + len(Fungi))