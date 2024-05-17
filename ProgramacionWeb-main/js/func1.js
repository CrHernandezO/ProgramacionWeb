$(document).ready(function () {
    $("#btnEnviar").click(function (event) {
        event.preventDefault();  // Evita el envío del formulario hasta que se validen los datos
        let rut = $("#txtRut").val();
        let nombre = $("#txtNombre").val();
        let appaterno = $("#txtAppaterno").val();
        let apmaterno = $("#txtApmaterno").val();
        let fecha = $("#txtFecha").val();
        let edad = $("#txtEdad").val();
        let genero = $("input[name=optGenero]:checked").val();
        let mail = $("#txtMail").val();
        let telefono = $("#txtTelefono").val();
        console.log(genero);

        if (validarDatos(rut, nombre, appaterno, apmaterno, edad, genero, telefono, mail, fecha)) {
            $("#formulario").submit();
        }
    });

    function validarDatos(rut, nombre, appaterno, apmaterno, edad, genero, celular) {

        if (String(rut).length < 9 || String(rut).length > 10) {
            /* Validacion Rut */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Rut debe tener largo entre 9 y 10 caracteres</div>");
        } else if (String(nombre).length < 3 || String(nombre).length > 20) {
            /* Validacion Nombre */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Nombre debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(appaterno).length <= 3 || String(appaterno).length >= 20) {
            /* Validacion Apellido Paterno */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Paterno debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(apmaterno).length <= 3 || String(apmaterno).length >= 20) {
            /* Validacion Apellido Materno */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Materno debe tener largo entre 3 y 20 caracteres</div>");
        } else if (Number(edad) < 18 && Number(edad) > 30) {
            /* Validacion Edad */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Edad debe estar entre 18 y 30 años</div>");
        } else if (genero != "Masculino" && genero != "Femenino" && genero != "Otro") {
            /* Validacion Genero */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Debe seleccionar un genero valido</div>");

        } else if (String(celular).length < 9 || String(celular).length > 12) {
            /* Validacion Edad */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Telefono debe tener entre 9 y 12 digitos</div>");
        } else if (!validateEmail(mail)) {
            /* Validacion Email */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center'>Debe ingresar un correo electronico valido</div>");
        } else if (!validateDate(fecha)) {
            /* Validacion Fecha */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center'>Debe ingresar una fecha valida en formato AAAA-MM-DD</div>");
        }  else {
            /* Confirmacion */
            $("#check").html("<div class='alert alert-success w-50 mx-auto text-center' >Datos Ingresado con exito</div>");

        }

    }
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    function validateDate(date) {
        const re = /^\d{4}-\d{2}-\d{2}$/;
        return re.test(date);
    }
});