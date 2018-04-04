$(document).ready(function() {

    $('.datetime-picker').daterangepicker({
      singleDatePicker: true,
      singleClasses: "picker_2",
      timePicker: true,
      timePickerIncrement: 30,
      locale: {
        format: 'MM/DD/YYYY h:mm A'
      }      
    }, function(start, end, label) {
      console.log(start.toISOString(), end.toISOString(), label);
    });
});