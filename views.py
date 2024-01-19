from app import app, db
from flask import render_template, redirect, flash, session, url_for, request
from methods import criar_tarefas, getMomento
from models import Usuario, Tarefas


@app.route("/")
def index():
    try:
        if session["usuario_logado"] != None and "usuario_logado" in session:
            return render_template("index.html", usuario=session["usuario_logado"].capitalize())
        else:
            return render_template("index.html", usuario=None)
    except:
        return render_template("index.html", usuario=None)


@app.route("/login")
def login():
    try:
        if session["usuario_logado"] != None and "usuario_logado" in session:
            flash(session["usuario_logado"] + " ainda está logado! Favor fazer logout!")
            return redirect(url_for("index"))
        else:
            proximo = request.args.get("proximo")
            return render_template("login.html", proximo=proximo, usuario=None)
    except:
        proximo = request.args.get("proximo")
        return render_template("login.html", proximo=proximo, usuario=None)


@app.route("/logout")
def logout():
    if session["usuario_logado"] != None and "usuario_logado" in session:
        session["usuario_logado"] = None
        flash("Logout realizado com sucesso!")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))



@app.route("/cadastro")
def cadastro():
    try:
        if session["usuario_logado"] != None and "usuario_logado" in session:
            flash(session["usuario_logado"] + " ainda está logado! Favor fazer logout!")
            return redirect(url_for("index"))
        else:
            return render_template("cadastro.html", usuario=None)
    except:
        return render_template("cadastro.html", usuario=None)


@app.route("/autenticar", methods=["POST", "GET"])
def autenticar():
    login = request.form["usuario"]
    senha = request.form["senha"]
    usuario = Usuario.query.filter_by(usuario=login).first()

    print(login, senha)
    if (len(senha) > 0):
        if senha == usuario.senha:
            session["usuario_logado"] = login.capitalize()
            flash(session["usuario_logado"] + " logado com sucesso!!")
            try:
                proximo = request.form["proximo"]
                return redirect(url_for(proximo))
            except:
                return redirect(url_for("index"))
        else:
            flash("Usuario ou senha está incorreto!!")
            return redirect(url_for('login', usuario=None))
    else:
        flash("Usuario ou senha está incorreto!!")
        return redirect(url_for('login', usuario=None))


@app.route("/adicionar", methods=["POST"])
def adicionar():
    try:
        if session["usuario_logado"] != None:
            tarefa = criar_tarefas()
            db.session.add(tarefa)
            db.session.commit()
            flash("Tarefa criada com sucesso!")
            return redirect(url_for("tarefas"))
        else:
            flash("Para criar novas tarefas, faça login primeiro!")
            proximo = "tarefas"
            return redirect(url_for("login", proximo=proximo))
    except:
        flash("Para criar novas tarefas, faça login primeiro!")
        proximo = "tarefas"
        return redirect(url_for("login", proximo=proximo))


@app.route("/tarefas", methods=["GET"])
def tarefas():
    try:
        if session["usuario_logado"] != None and "usuario_logado" in session:
            print("O usuario logado é:" + session["usuario_logado"])
            usuario = Usuario.query.filter_by(usuario=session["usuario_logado"]).first()
            tarefas = Tarefas.query.filter_by(usuario_id=usuario.id).all()
            print(tarefas)
            if (len(tarefas) > 0):
                return render_template("tarefas.html", listTask=tarefas, usuario=session["usuario_logado"])
            else:
                return render_template("tarefas.html", listTask=None, usuario=session["usuario_logado"])
        else:
            return render_template("tarefas.html", listTask=None, usuario=None)
    except:
        return render_template("tarefas.html", listTask=None, usuario=None)


@app.route("/delete/<int:id>")
def delete(id):
    task = Tarefas.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tarefas"))


@app.route("/tarefa/<int:id>", methods=["GET", "POST"])
def tarefa_view(id):
    if request.method == "GET":
        tarefa = Tarefas.query.get(id)
        return render_template("tarefa_view.html", tarefa=tarefa, usuario=session["usuario_logado"])
    else:
        print(request.method)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    tarefa = Tarefas.query.get(id)
    if request.method == 'POST':
        tarefa.tarefa = request.form['tarefa']
        tarefa.descricao = request.form['descricao']
        data, hora = getMomento()
        tarefa.data = data
        tarefa.hora = hora
        db.session.commit()
        return redirect(url_for("tarefa_view", id=id))

@app.route('/alterar_dados_valida', methods=['POST', 'GET'])
def alterar_dados_valida():
    novo_usario = request.form['novo_usuario']
    nova_senha = request.form['nova_senha']
    confirma_senha = request.form['confirma_senha']
    if (Usuario.query.filter_by(usuario=novo_usario).first()):
        flash('Usuario já existente!!')
        return redirect(url_for('index', usuario=session["usuario_logado"]))
    else:
        if nova_senha == confirma_senha:
            usuario = Usuario.query.filter_by(usuario=session["usuario_logado"]).first()
            usuario.usuario = novo_usario
            usuario.senha = nova_senha
            session["usuario_logado"] = novo_usario
            db.session.commit()
            flash('Dados alterados com sucesso!!')
            return redirect(url_for('index', usuario=session["usuario_logado"]))
        else:
            flash('Senhas não correspondem!!')
            return redirect(url_for('alterar_dados', usuario=session["usuario_logado"]))

@app.route("/alterar_dados", methods=['POST', 'GET'])
def alterar_dados():
    return render_template('alterar_dados.html', usuario=session["usuario_logado"])

@app.route("/cadastro_usuario", methods=['POST'])
def cadastro_usuario():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        confirma_senha = request.form['confirma_senha']
        if len(usuario) <= 0 or len(senha) <=0:
            flash('Informe os campos solicitados!!')
            return redirect(url_for('cadastro', usuario=None, mensagem='Usuario já existente!!'))
        else:
            if (Usuario.query.filter_by(usuario=usuario).first()):
                flash('Usuario já existente!!')
                return redirect(url_for('cadastro', usuario=None))
            else:
                if confirma_senha == senha:
                    usuario = Usuario(usuario=usuario, senha=senha)
                    db.session.add(usuario)
                    db.session.commit()
                    flash('Conta criada com sucesso!')
                    return redirect(url_for('index'))
                else:
                    flash('Senhas não correspondem!!')
                    return redirect(url_for('cadastro', usuario=None))

