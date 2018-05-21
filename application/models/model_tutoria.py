import web
import config

db = config.db


def get_all_tutoria():
    try:
        return db.select('tutoria')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_tutoria(id_tutoria):
    try:
        return db.select('tutoria', where='id_tutoria=$id_tutoria', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_tutoria(id_tutoria):
    try:
        return db.delete('tutoria', where='id_tutoria=$id_tutoria', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_tutoria(alumno,tutor,carrera,grupo,area_tutoria,nombre_responsable,acciones,resolucion,fecha):
    try:
        return db.insert('tutoria',alumno=alumno,
tutor=tutor,
carrera=carrera,
grupo=grupo,
area_tutoria=area_tutoria,
nombre_responsable=nombre_responsable,
acciones=acciones,
resolucion=resolucion,
fecha=fecha)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_tutoria(id_tutoria,alumno,tutor,carrera,grupo,area_tutoria,nombre_responsable,acciones,resolucion,fecha):
    try:
        return db.update('tutoria',id_tutoria=id_tutoria,
alumno=alumno,
tutor=tutor,
carrera=carrera,
grupo=grupo,
area_tutoria=area_tutoria,
nombre_responsable=nombre_responsable,
acciones=acciones,
resolucion=resolucion,
fecha=fecha,
                  where='id_tutoria=$id_tutoria',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
