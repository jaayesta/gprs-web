//El SOCKET
var socket = io.connect('http://server.drivetech.cl:22988');

socket.on('connect', function () {
    //socket connected
    console.log("Socket connected");
});

socket.on('new data', function (data){
    alert(data.toString());
    attach_data(data);
});

function attach_data(data){
    var table=document.getElementById("gprs");
    var row=table.insertRow(0);
    var cell1=row.insertCell(0);
    var cell2=row.insertCell(1);
    cell1.innerHTML=get_time();
    cell2.innerHTML=data.toString();
}

function get_time(){
    var marcacion = new Date()
    var Hora = marcacion.getHours()
    var Minutos = marcacion.getMinutes()
    var Segundos = marcacion.getSeconds()

    if (Hora<=9){
        Hora = "0" + Hora;
    }
    if (Minutos<=9){
        Minutos = "0" + Minutos;
    }
    if (Segundos<=9){
        Segundos = "0" + Segundos;
    }
    var Hoy = new Date();
    var Dia = Hoy.getDate();
    var Mes = Hoy.getMonth() + 1;
    var Anio = Hoy.getFullYear().toString().substring(2);

    if(Dia<=9){
        Dia = "0" + Dia;
    }
    if(Mes<=9){
        Mes = "0" + Mes;
    }

    var Fecha = Hora.toString() + ":" + Minutos.toString() +":" + Segundos.toString();
    return Fecha;
}