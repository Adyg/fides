var Fides = {};

(function ( $ ) {
  /**
  * Handles date range selects
  *
  */
  Fides.initDatePicker = function($input) {
    $input.daterangepicker({
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
  };


  /**
  * Handles datatable bulk actions
  */ 
  Fides.datatableActions = function($container) {
    var $bulkRemoveTrigger = $container.find('.bulk-page-remove'),
        tableRecordsName = 'table_records';

    var bulkDelete = function() {
      $bulkRemoveTrigger.on('click', function(e){
        e.preventDefault();
        var $this = $(this);

        var $selectedInputs = $container.find('input[name="'+tableRecordsName+'"]:checked'),
            tableRecordIds = [],
            commaSeparatedTableRecordIds = '';
        console.log($selectedInputs);
        $selectedInputs.each(function($element){
          tableRecordIds.push($element.val());
        });

        commaSeparatedTableRecordIds = tableRecordIds.join(',');
        var deleteUrl = $this.attr('href') + '?page_ids='+commaSeparatedTableRecordIds;
        window.location = deleteUrl;
      });
    }

    bulkDelete();
  };

  /**
  * Inits
  */
  Fides.initDatePicker($('.datetime-picker'));
  Fides.datatableActions($('table.bulk_action'));

}(jQuery));