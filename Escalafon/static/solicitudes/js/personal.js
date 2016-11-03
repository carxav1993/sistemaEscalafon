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
			$("#requisitos").html("<tr><th>Requisitos</th><th>Evidencias</th><th>Archivos</th></tr>");
			for (var i = 0; i < data.length; i++) {
				$("#requisitos").append("<tr><td>"+data[i].fields.nombre+"</td><td><p>Evidencia aquí</p></td><td><label class=''>Seleccione archivo</label><input name='archi"+i+"' type='file' class=''></td></tr>");
			}
		}
	});
}