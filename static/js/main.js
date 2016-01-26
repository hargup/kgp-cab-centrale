$(document).ready(function() {
    $('select').material_select();
});

$('#id_date').datepicker({
    language: 'en',
    todayButton : true,
    clearButton : true,
    autoClose : true,
});

$('#id_date').datepicker().data("datepicker").selectDate(new Date()) // Set todays date by default

$('#id_form_dob').datepicker({
    language: 'en',
    todayButton : true,
    clearButton : true,
    autoClose : true,
	position : "left bottom",
});

$('#id_summary').focus(function() {
	$('#mdsupport').text("The editor is markdown flavored");
});
