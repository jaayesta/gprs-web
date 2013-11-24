# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from settings import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_USER_PASSWORD, DATABASE_NAME
from pymongo import Connection, ASCENDING, DESCENDING
import tablib
from django.contrib.auth.decorators import login_required

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


def export_to_excel(request):
    """
    Devuelve un excel con todos los datos de la base de datos.
    """
    db = connect_to_mongo()
    if db:
        gprs = get_data(db)
    else:
        gprs = None
        print("Error connection to mongo")
    if gprs:
        headers = ('Fecha', 'Hora', 'Dato')
        data = []
        data = tablib.Dataset(*data, headers=headers)
        for obj in gprs:
            data.append((obj['date'], obj['time'], obj['gprs']))

        response = HttpResponse(data.xls, content_type='application/vnd.ms-excel;charset=utf-8')
        response['Content-Disposition'] = "attachment; filename=gprs.xls"

        return response
    else:
        return render_to_response('error.html', {'message': 'No hay datos para exportar'}, context_instance=RequestContext(request))

@login_required
def admin_database(request):
    if not request.method == 'POST':
        return render_to_response('admin.html', {'success': None }, context_instance=RequestContext(request))
    else:
        success = delete_data()
        return render_to_response('admin.html', {'success': success}, context_instance=RequestContext(request))



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

def delete_data():
    db = connect_to_mongo()
    if db:
        try:
            coll = db['gprs']
            coll.remove()
            return True
        except:
            print 'Error eliminando la informacion de la base de datos'
            return False
    else:
        return False