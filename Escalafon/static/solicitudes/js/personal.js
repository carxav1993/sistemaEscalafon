$("#ddUA").on('change', traerCarrera);
function traerCarrera(){
	var codigo = $("#ddUA").val();
	console.log('id: '+codigo);
	//console.log($("#txtFechaIngresoU").val());
	$.ajax({
		data : {'codigo':codigo},
		url : '/traerCarreras/',
		type : 'get',
		success : function(response){
			$("#ddCarreras").html("");
			for (var i = 0; i < response.length; i++) {
				$("#ddCarreras").append("<option value='"+response[i].pk+"'>"+(response[i].fields.nombre)+"</option>");
			}
		}
	});
}

$("#ddCategoriaAspirada").on('change', traerRequisitos);
function traerRequisitos(){
	var id = $("#ddCategoriaAspirada").val();
	console.log("Categoria: " + id);
	$.ajax({
		data : {'id':id},
		url : '/traerRequisitos/',
		type : 'get',
		success : function(data){
			console.log(data);
			$("#requisitos").html("<tr><th>Requisitos</th><th>Archivos</th></tr>");
			for (var i = 0; i < data.length; i++) {
				$("#requisitos").append("<tr><td>"+data[i].fields.nombre+"</td><td><label class=''>Seleccione archivo</label><input name='archi"+i+"' type='file' class=''></td></tr>");
			}
		}
	});
}

$("#btnGenerar").on('click', validar);
function validar(){
	var nombres = $("#txtNombres").val();
	var apellidos = $("#txtApellidos").val();
	var cedula = $("#txtCedula").val();
	var email = $("#txtEmail").val();
	var unidadAcademica = $("#ddUA").val();
	var carrera = $("#ddCarreras").val();
	var categoriaActual = $("#ddCategoriaActual").val();
	var categoriaAspirada = $("#ddCategoriaAspirada").val();
	var fechaIngreso = $("#txtFechaIngresoU").val();

	var fecha = new Date();
		fechaActual = (fecha.getFullYear() +"-"+ (fecha.getMonth() + 1) +"-"+fecha.getDate());

	console.log("Datos recogidos del formulario: "+nombres+" - "+apellidos+" - "+cedula+" - "+email+" - "+unidadAcademica
		+" - "+carrera+" - "+categoriaActual+" - "+categoriaAspirada+" - "+fechaIngreso+" - "+fechaActual);
	$.ajax({
		data : {'nombres':nombres, 'apellidos':apellidos, 'cedula':cedula, 'email':email, 'ua':unidadAcademica,
				'carrera':carrera, 'cac':categoriaActual, 'cas':categoriaAspirada, 'fi':fechaIngreso, 'fs':fechaActual},
		url : '/anadirPersonal/',
		type : 'get',
		success : function(data){
			
		}
	});
}