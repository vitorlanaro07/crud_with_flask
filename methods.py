import datetime
from models import Tarefas, Usuario
from flask import request, session

def getMomento():
    agora = datetime.datetime.now()
    if len(str(agora.day)) <= 1:
        dia = "0" + str(agora.day)
    else:
        dia = str(agora.day)

    if len(str(agora.month)) <= 1:
        mes = "0" + str(agora.month)
    else:
        mes = str(agora.month)

    if len(str(agora.hour)) <= 1:
        hora = "0" + str(agora.hour)
    else:
        hora = str(agora.hour)

    if len(str(agora.minute)) <= 1:
        minuto = "0" + str(agora.minute)
    else:
        minuto = str(agora.minute)

    if len(str(agora.second)) <= 1:
        segundo = "0" + str(agora.second)
    else:
        segundo = str(agora.second)

    data = dia + "/" + mes + "/" + str(agora.year)
    tempo = hora + ":" + minuto + ":" + segundo

    return data, tempo

def criar_tarefas():
    tarefa = request.form['tarefa']
    descricao = request.form['descricao']
    data, hora = getMomento()
    usuario_id = Usuario.query.filter_by(usuario=session["usuario_logado"]).first().id
    return Tarefas(tarefa, descricao, data, hora, usuario_id)

