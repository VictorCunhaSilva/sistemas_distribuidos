nome_do_arquivo = input('Nome do arquivo a ser editado:')
arquivo = open(nome_do_arquivo, 'w')
texto = open(nome_do_arquivo, 'r')
string2 = input('Insira o texto:')
#arquivo = 
arquivo.writelines(texto)
arquivo.writelines(string2)
arquivo.close()
