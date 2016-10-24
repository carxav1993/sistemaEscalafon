$("#ddUA").on('change', traerCarrera);
function traerCarrera(){
	var codigo = $("#ddUA").val();
	console.log('id: '+codigo);
	console.log($("#txtFechaIngresoU").val());
	$.ajax({
		data : {'codigo':codigo},
		url : '/traerCarreras/',
		type : 'get',
		success : function(response){
			$("#ddCarreras").html("");
			for (var i = 0; i < response.length; i++) {
				$("#ddCarreras").append("<option value='"+response[i].pk+"'>"+(response[i].fields.nombre)+"</option>");
				// console.log(response[i].fields.nombre);
				// console.log(response[i].pk);
			}
		}
	});
}