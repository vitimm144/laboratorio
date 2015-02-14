$(function(){
    $("#paciente_chosen").change( function(evt, obj){
        $('.modal-content').append(
            "<div id='edit'><a data-toggle='modal' "+
            "href='http://localhost:8000/atendimento_paciente/"+ obj['selected'] +"/' "+
            "data-target='#form-modal-edit' id='modal_edit' "+
            "data-backdrop='static' "+
            "data-keyboard='false'></a></div>"
        )
        $('#modal_edit').trigger('click')

    });
})
