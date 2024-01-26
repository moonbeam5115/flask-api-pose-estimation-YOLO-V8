document.addEventListener('DOMContentLoaded', function() {


    // var event_date = new Date(dateStr + 'T07:00:00')
    var nice_yellow = {"background-color": 'rgba(255, 179, 0, 0.5)'}


    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      headerToolbar: { center: 'dayGridMonth, timeGridSingleDay, addEventButton' },
      showNonCurrentDates: false,
      editable: true,      
      eventBackgroundColor: 'rgba(255,179,0, 0.5)',
      eventTextColor: 'black',
      dayMaxEventRows: 2,
      customButtons: {
        addEventButton: {
          text: 'Add Workout',
          click: function() {
            
            // Collect information from #Calendar element
            let information = $("#calendar").data("date")
            console.log("Testing Javascript logic...")
            console.log($("#calendar").data)
            
            if (typeof(information) !== 'undefined') { // valid?
              // Unbind modal to unbind dateClick data from previous clicks
              // $("#myModal").unbind();

              // Launch + show Modal
              $("#myModal").modal('show');

              // After Modal Shows
              $('#myModal').on('shown.bs.modal', function modal_func (e) {
                // When Clicking on Add Button - Make sure it only runs One Time
                $("button#add_btn").off('click').one('click', function(e) {                  
                  
                  // Add Workout to Events
                  e.preventDefault(); // prevent page from reloading bug
                  let dateStr = information.dateStr;
                  let date = new Date(dateStr + 'T07:00:00'); // will be in local time
                  
                  // alert user if data fields are empty
                  if ($("#exercise_01").val() == "") {
                    alert("Please write an exercise")
                    modal_func(e)
                  }
                  else {
                    calendar.addEvent({
                      title: 'Workout',
                      start: date
                    });
                    $('a.fc-daygrid-dot-event').css(nice_yellow)

                    // Get Data from Modal Input Boxes
                    var workout_row = []
                    var workout_obj = new Object();
                    var workout_form_data = []
                    
                    $('.form-control').each(function(key) {
                      //console.log(key)
                      workout_row.push($(this).val())

                      // Check for every 3rd input box
                      if ((key+1) % 3 == 0){
                        workout_obj['exercise ' + ((key+1)/3)] = workout_row[0];
                        workout_obj['sets'] = workout_row[1];
                        workout_obj['reps'] = workout_row[2];
                        // append workout obj to workout_form_data array and reset workout_row & workout_obj
                        workout_form_data.push(workout_obj);
                        workout_row = [];
                        workout_obj = new Object();
                        //console.log('row ' + (key+1))
                      }

                    })

                    // Add date to workout_form_data
                    date_wo_event = {
                      wo_event :  workout_form_data,
                      event_date: dateStr
                    }

                    // Use Fetch to POST request to calendar/workout_event
                    fetch(`${window.origin}/myCalendar/workout_event`, {
                      method: "POST",
                      credentials: "include",
                      body: JSON.stringify(date_wo_event),
                      cache: "no-cache",
                      headers: new Headers({
                        "content-type": "application/json"
                      })

                    })
                    .then(response => response.json())
                    .then(res_data => console.log(res_data));
                    
                    // Hide Modal
                    $('#myModal').modal('hide');
                  }
                  

                });

              });
              
              // On Modal Hidden
              $("#myModal").on('hidden.bs.modal', function (e) {
                // Clear data from Modal fields
                $(this)
                .find("input,textarea,select")
                   .val('')
                   .end()
                .find("input[type=radio]")
                   .prop("checked", "")
                   .end();
                
                
                $('a.fc-daygrid-dot-event').css({"background-color": 'rgba(255, 179, 0, 0.5)'})
                console.log("clicky clicky");
              
              });

            } else {
              alert('Pick a date');
            }
          }
        }
      },
      initialView: 'dayGridMonth',
      views: {
        timeGridSingleDay: { // name of view
          // other view-specific options here
          type: 'timeGrid',
          duration: { days: 1},
          buttonText: 'Day'
        }
      },
      eventClick: function(info) {
        
        info.el.style.backgroundColor = "rgb(51, 204, 51)";

        // TODO: update DB to toggle workout complete
        
      },
      dateClick: function(info) {
        
        // Check for previously clicked dates
        dateObject = $("#calendar").data("date");
        
        // console.log($("#calendar").data("date"))
        
        if (typeof(dateObject) != 'undefined') {
          // Get PREVIOUSLY selected date and reset background color
          let prevSelect = $("#calendar").data("date")
          prevSelect.dayEl.style.backgroundColor = "";
        }

        // Set CURRENT selected date background color
        info.dayEl.style.backgroundColor = "rgba(137, 196, 244, 0.25)";
        
        // Set CURRENT selected date to #Calendar element data - "date"
        $("#calendar").data("date", info);
        // console.log($("#calendar").data("date"))
      },
      slotDuration: '01:00:00',
      slotMinTime: '06:00:00',
      slotMaxTime: '18:00:00',
      selectable: false
    });

    
    // Render Calendar Elements
    calendar.render();
    
    // Delete unnecessary button elements
    $('.fc--button').each(function(key) {
      $(this).remove();
    })

    $.getJSON('/myCalendar/workout_event', function(response) {

      event_source = {
        events: [
        ]  
        }

      console.log("RESPONSE: ")
      console.log(response)
      
      idx = 0
      for (property in response) {
        console.log(property)
        console.log(response[property].all_workouts)
        console.log(response[property].date)

        var dateStr = response[property].date
        var event_date = new Date(dateStr + 'T07:00:00')
        event_source.events.push({
              title: 'workout',         //TODO: Programatically change title
              start: event_date
        })

        calendar.addEvent(event_source.events[idx])
        idx += 1

      }
      
      
        

    })    
    
    calendar.render();

  });