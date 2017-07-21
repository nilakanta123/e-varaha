$(document).ready(function(){

    $('#decision_switch').bootstrapSwitch();
    $('#decision_switch').on('switchChange.bootstrapSwitch', function(event, state) {
        console.log(this); // DOM element
        console.log(event); // jQuery event
        console.log(state); // true | false
    });

    // Django generated form id
    $('#id_type_of_organisms').multiselect({
        maxHeight: 200,
        buttonWidth: '100%',
        numberDisplayed: 10,
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_type_of_organisms').change(function (e) {
        e.preventDefault();
        $.ajax({
            url:"/ajax_request/",
            type:"POST",
            data: { post_table : $('#id_type_of_organisms').val() },
            cache: false,
            dataType: "json",
            success: function(json){
                $('#message').text(json.table);
                updateSelect( $('#id_age_group'), json.age);
                updateSelect( $('#id_system_affected'), json.system);
                updateSelect( $('#id_organ_affected'), json.organ);
                updateSelect( $('#id_causative_agent'), json.agent);
                updateSelect( $('#id_disease_condition'), json.disease);
                updateSelect( $('#id_am_findings'), json.am);
                updateSelect( $('#id_pm_findings'), json.pm);
            }
        });
        return false;
   
    });
    $('#id_age_group').multiselect({
        maxHeight: 200,
        buttonWidth: '100%',
        numberDisplayed: 10,
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_system_affected').multiselect({
        maxHeight: 200,
        buttonWidth: '100%',
        numberDisplayed: 10,
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_organ_affected').multiselect({
        maxHeight: 200,
        buttonWidth: '100%',
        numberDisplayed: 10,
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_causative_agent').multiselect({
        maxHeight: 200,
        buttonWidth: '100%',
        numberDisplayed: 10,
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_disease_condition').multiselect({
        maxHeight: 200,
        buttonWidth: '100%',
        numberDisplayed: 10,
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_am_findings').multiselect({
        maxHeight: 200,
        buttonWidth: '100%',
        numberDisplayed: 10,
        enableCaseInsensitiveFiltering: true,
    });
    $('#id_pm_findings').multiselect({
        maxHeight: 200,
        buttonWidth: '100%',
        numberDisplayed: 10,
        enableCaseInsensitiveFiltering: true,
    });
    
    // smooth scroll link id
    $("#about-link").click(function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#about").offset().top
        }, 700);
    });
    $("#dss-link").click(function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#dsstable").offset().top+53
        }, 700);
    });
    $("#home-link").click(function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#myCarousel").offset().top
        }, 700);
    });
    $("#logo").click(function(e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $("#myCarousel").offset().top
        }, 700);
    });
    
    function updateSelect(id, options){  
        option ="<option value=''>None selected</option>";
        $.each(options, function(key, obj){ option+="<option value="+obj.value+">"+obj.label+"</option>"; });
        id.children().remove().end().append(option);
        id.multiselect('rebuild');
    }

});
