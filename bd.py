login = {'Rod':'1234',
         'Gui': '4321'}

disciplinas = {'Rod': [['ltp1', 5, 6.7, 7.8], ['lab_1', 10, 8, 9.5]],
               'Gui': [['Citologia', 5, 6.7, 7.8], ['Botânica', 10, 8, 9.5]]}

detalhes = {'ltp1': 'Disciplina LTP1 , Professor: Juca',
            'lab_1': 'Disciplina Laboratorio de Programação 1, Professor: Cleuber',
            'Citologia': 'Disciplina Citologia ,Professor: Cleuber',
            'Botânica': 'Disciplina Botânica ,Professora: Juana'}

def validar_login(usuario, senha):
    return (usuario in login) and (login[usuario] == senha)

def get_diciplinas(usuario):
    return disciplinas[usuario]

def get_detalhes(materia):
    return detalhes[materia]

