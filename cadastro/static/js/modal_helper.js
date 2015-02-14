$(function(){
    $("#paciente_chosen").change( function(evt, obj){
        console.log(obj['selected']);
        $('.modal-content').append(
            "<div id='edit'><a data-toggle='modal' "+
            "href='http://localhost:8000/atendimento_paciente/"+ obj['selected'] +"/' "+
            "data-target='#form-modal-edit' id='modal_edit' "+
            "data-backdrop='static' "+
            "data-keyboard='false'></a></div>"
        )
        $('#modal_edit').trigger('click')

    });
    $('#above_remove').on('click', function(){
        $('#teste').remove()
    });
    $('#bellow_remove').on('click', function(){
        $('#edit').remove()
    });

})
