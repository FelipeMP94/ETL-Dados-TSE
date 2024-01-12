import pandas as pd

dado_total = pd.read_csv(r"C:\Users\Felipe\Documents\Dados TSE\perfil_eleitor_secao_ATUAL_SP\perfil_eleitor_secao_ATUAL_SP.csv",encoding = 'latin1',sep = ';')

def Quantidade_por_grau_escolaridade(zona):
    qt_escolaridade = {}
    qt = 0 
    for grau in zona['DS_GRAU_ESCOLARIDADE'].unique():
        for row in zona[zona['DS_GRAU_ESCOLARIDADE']== grau ].itertuples():
            qt += row.QT_ELEITORES_PERFIL
        qt_escolaridade[grau] = qt
        qt = 0
    return qt_escolaridade


def Quantidade_por_faixa_etaria(zona):
    qt_faixa_etaria = {}
    qt = 0  
    for faixa in zona['DS_FAIXA_ETARIA'].unique():
        for row in zona[zona['DS_FAIXA_ETARIA']== faixa ].itertuples():
            qt += row.QT_ELEITORES_PERFIL
        qt_faixa_etaria[faixa] = qt
        qt = 0
    return qt_faixa_etaria



def Quantidade_por_estado_civil(zona):
    qt_estado_civil = {}
    qt = 0 
    for estado in zona['DS_ESTADO_CIVIL'].unique():
        for row in zona[zona['DS_ESTADO_CIVIL']== estado ].itertuples():
            qt += row.QT_ELEITORES_PERFIL
        qt_estado_civil[estado] = qt
        qt = 0
    return qt_estado_civil



def Quantidade_por_genero(zona):
    qt_genero = {}
    qt = 0 
    for t_gen in zona['DS_GENERO'].unique():
        for row in zona[zona['DS_GENERO']== t_gen ].itertuples():
            qt += row.QT_ELEITORES_PERFIL
        qt_genero[t_gen] = qt
        qt = 0
    return qt_genero

#Principal 

dados_zonas_eleitorais = []

for z in dado_total['NR_ZONA'].unique():
    zona = dado_total[dado_total['NR_ZONA']== z]
    info_zonas = {'id_zona':z ,
                 'Escolaridade': Quantidade_por_grau_escolaridade(zona),
                 'Faixa Etaria':Quantidade_por_faixa_etaria(zona),
                 'Estado_Civil':Quantidade_por_estado_civil(zona),
                 'Genero':Quantidade_por_genero(zona)
                 }
    
    dados_zonas_eleitorais.append(info_zonas)

print(dados_zonas_eleitorais)


