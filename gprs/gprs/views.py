# -*- encoding: utf-8 -*-
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from settings import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_USER_PASSWORD, DATABASE_NAME
from pymongo import Connection, ASCENDING, DESCENDING


def home(request):
    """
    Se muestra la informacion en tiempo real
    """
    return render_to_response("index.html", {}, context_instance=RequestContext(request))


def stored(request):
    """
    Devuelve una tabla con todos los datos guardados en la base de datos
    """
    db = connect_to_mongo()
    if db:
        data = get_data(db)
    else:
        data = None
        print("Error connection to mongo")
    return render_to_response('stored.html', {'data': data}, context_instance=RequestContext(request))


def connect_to_mongo():
    """
    Metodo que crea la coneccion con la base de datos mongodb
    """
    try:
        connection = Connection(MONGO_HOST, MONGO_PORT)
        db = connection[DATABASE_NAME]
        db.authenticate(MONGO_USER, MONGO_USER_PASSWORD)
        print("Authentication success")
        return db
    except:
        print("Error connecting to mongoDB")
        db = None
        return db


def get_data(db):
    """
    Obtiene los datos de la collection de mongo
    """
    data = []
    try:
        coll = db['gprs']
        gprs_list = coll.find({}, sort=[("_id", DESCENDING)])
        for doc in gprs_list:
            date = doc['date']
            time = doc['time']
            data.append({'date': date, 'time': time, 'gprs': doc['data']})
    except:
        print("Error getting data from mongodb")
    return data