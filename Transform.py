import pandas as pd
import time

dado_total = pd.read_csv(r"C:\Users\Felipe\Documents\Dados TSE\perfil_eleitor_secao_ATUAL_SP\perfil_eleitor_secao_ATUAL_SP.csv",encoding = 'latin1',sep = ';')

def Quantidade_por_grau_escolaridade(zona):
    qt_escolaridade = {}
    for grau in zona['DS_GRAU_ESCOLARIDADE'].unique():
        dataloc = zona.loc[zona['DS_GRAU_ESCOLARIDADE']== grau]
        qt_escolaridade[grau] = dataloc['QT_ELEITORES_PERFIL'].sum()
    return qt_escolaridade


def Quantidade_por_faixa_etaria(zona):
    qt_faixa_etaria = {}
    for faixa in zona['DS_FAIXA_ETARIA'].unique():
        dataloc =  zona.loc[zona['DS_FAIXA_ETARIA']== faixa ]
        qt_faixa_etaria[faixa] = dataloc['QT_ELEITORES_PERFIL'].sum()
    return qt_faixa_etaria



def Quantidade_por_estado_civil(zona):
    qt_estado_civil = {}
    for estado in zona['DS_ESTADO_CIVIL'].unique():
        dataloc =  zona.loc[zona['DS_ESTADO_CIVIL']== estado ]
        qt_estado_civil[estado] = dataloc['QT_ELEITORES_PERFIL'].sum()
    return qt_estado_civil



def Quantidade_por_genero(zona):
    qt_genero = {}
    for t_gen in zona['DS_GENERO'].unique():
        dataloc =  zona.loc[zona['DS_GENERO']== t_gen ]
        qt_genero[t_gen] = dataloc['QT_ELEITORES_PERFIL'].sum()
    return qt_genero

#Principal 

dados_zonas_eleitorais = []
ini = time.time()
for z in dado_total['NR_ZONA'].unique():
    zona = dado_total[dado_total['NR_ZONA']== z]
    info_zonas = {'id_zona':z ,
                 'Escolaridade': Quantidade_por_grau_escolaridade(zona),
                 'Faixa Etaria':Quantidade_por_faixa_etaria(zona),
                 'Estado_Civil':Quantidade_por_estado_civil(zona),
                 'Genero':Quantidade_por_genero(zona)
                 }
    
    dados_zonas_eleitorais.append(info_zonas)
fim = time.time()
print(fim-ini)


