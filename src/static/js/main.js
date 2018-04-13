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

        $selectedInputs.each(function(it){
          tableRecordIds.push($(this).val());
        });

        commaSeparatedTableRecordIds = tableRecordIds.join(',');
        var deleteUrl = $this.attr('href') + '?page_ids='+commaSeparatedTableRecordIds;
        window.location = deleteUrl;
      });
    }

    bulkDelete();
  };


  /**
  * Handles creating formset items
  *
  */
  Fides.formset = function($formset, prefix) {
    console.log('formset');
    var cloneFormset = function($formset, prefix) {
      console.log('clone formset');
      var $trigger = $formset.find('.add-formset-item'),
          $formsetItem = $formset.find('.formset-item:last');

      $trigger.on('click', function(){
        console.log('click');
        var $newElement = $formsetItem.clone(true),
            $inputTotal = $('#id_' + prefix + '-TOTAL_FORMS'),
            total = $inputTotal.val();

        $newElement.find(':input').each(function() {
            var name = $(this).attr('name').replace('-' + (total-1) + '-', '-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });

        total++;
        $inputTotal.val(total);

        $formsetItem.after($newElement);

        return false;
      });
    }

    cloneFormset($formset, prefix);
  }


  /**
  * Inits
  */
  Fides.initDatePicker($('.datetime-picker'));
  Fides.datatableActions($('table.bulk_action'));
  Fides.formset($('#previsual-assesment-formset'), 'form');

}(jQuery));