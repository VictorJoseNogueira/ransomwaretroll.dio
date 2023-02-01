import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('ocuto.txt', atributo_ocultar)

if retorno:
    print('arquivo foi ocultado')

else:
    print('arquivo nao ocultado')
