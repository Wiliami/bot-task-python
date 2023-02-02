from IPython.display import display

import tabula

lista_tabelas = tabula.read_pdf("Boleto.pdf", pages="all")
print(len(lista_tabelas))


for tabela in lista_tabelas:
    display(tabela)