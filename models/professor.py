from unicodedata import normalize


def remover_acentos(txt, codif='utf-8'):
    if isinstance(txt, unicode):
        txt = txt.encode('utf-8')
    return normalize('NFKD', txt.decode(codif)).encode('ASCII', 'ignore')







def lista_opcoes(cod_tabela):
    resultados = api.get('tab_estruturada', {'cod_tabela': cod_tabela, 'lmin': 0, 'lmax':999}, ['descricao'])
    return [remover_acentos(resultado['descricao'].strip()) for resultado in resultados]

OPCOES_ETNIAS =509
OPCOES_DEFICIENCIAS =229
OPCOES_NACIONALIDADES = 163
OPCOES_ESCOLARIDADES = 168

etnias = lista_opcoes(OPCOES_ETNIAS)
deficiencias = lista_opcoes(OPCOES_DEFICIENCIAS)
nacionalidades = lista_opcoes(OPCOES_NACIONALIDADES)
escolaridade = lista_opcoes(OPCOES_ESCOLARIDADES)


db.define_table('professores',
                Field('nome', requires=IS_NOT_EMPTY()),
                Field('cpf', requires=IS_NOT_EMPTY()),
                Field('estado_civil'),
                Field('sexo', requires=IS_IN_SET(['Masculino', 'Feminino'])),
                Field('escolaridade', requires=IS_IN_SET(escolaridade)),
                Field('data_nascimento', 'date', requires=IS_NOT_EMPTY(), label='Data de Nascimento'),
                Field('tipo_sanguineo', label='Tipo Sanguineo'),
                Field('etnia', requires=IS_IN_SET(etnias)),
                Field('deficiencia', requires=IS_IN_SET(deficiencias)),
                Field('naturalidade'),
                Field('nacionalidade', requires=IS_IN_SET(nacionalidades)),
                )
