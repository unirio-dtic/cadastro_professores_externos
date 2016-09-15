# coding=utf-8
from unicodedata import normalize


def remover_acentos(txt, codif='utf-8'):
    if isinstance(txt, unicode):
        txt = txt.encode('utf-8')
    return normalize('NFKD', txt.decode(codif)).encode('ASCII', 'ignore')







def lista_opcoes(cod_tabela):
    '''
     Consulta o endpoint tab_estruturada e retorna uma lista de descrições referentes a cod_tabela
    '''
    semana = 1209600
    where = {
        'cod_tabela': cod_tabela,
        'item_tabela_min': 0,  # descarta a descricao
        'lmin': 1,
        'lmax': 999
    }
    resultados = api.get('tab_estruturada', where, ['descricao'], cache_time=semana)
    return [remover_acentos(resultado['descricao'].strip()) for resultado in resultados]

OPCOES_ETNIAS = 509
OPCOES_DEFICIENCIAS = 229
OPCOES_NACIONALIDADES = 163
OPCOES_ESCOLARIDADES = 168
OPCOES_ESTADO_CIVIL = 162
OPCOES_ESTADOS = 206
OPCOES_TIPOS_SANGUINEOS = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']

db.define_table('professores',
                Field('nome', requires=IS_NOT_EMPTY()),
                Field('cpf', requires=IS_NOT_EMPTY()),
                # todo: Adicionar passaporte
                Field('estado_civil', requires=IS_IN_SET(lista_opcoes(OPCOES_ESTADO_CIVIL))),
                Field('sexo', requires=IS_IN_SET(['Masculino', 'Feminino'])),
                Field('escolaridade', requires=IS_IN_SET(lista_opcoes(OPCOES_ESCOLARIDADES))),
                Field('data_nascimento', 'date', requires=IS_NOT_EMPTY(), label='Data de Nascimento'),
                Field('tipo_sanguineo', requires=IS_IN_SET(OPCOES_TIPOS_SANGUINEOS), label='Tipo Sanguineo'),
                Field('etnia', requires=IS_IN_SET(lista_opcoes(OPCOES_ETNIAS))),
                Field('deficiencia', requires=IS_IN_SET(lista_opcoes(OPCOES_DEFICIENCIAS))),
                Field('naturalidade', requires=IS_IN_SET(lista_opcoes(OPCOES_ESTADOS))),
                Field('nacionalidade', requires=IS_IN_SET(lista_opcoes(OPCOES_NACIONALIDADES))),
                )
