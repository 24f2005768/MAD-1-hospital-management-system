// to hide or show different department doctors while booking an appointment
function hideShowDept(dept_id) {
    var dept_doctors = document.getElementsByClassName(dept_id);
    var all_doc = document.getElementsByClassName('all_doctors');
    for (doc of all_doc) {
        if (doc.classList.contains(dept_id)) {
            doc.style.display = 'block';
        }

        else {
            doc.style.display = 'none';
        }
    }

}

// for doctor dashboard 

var this_doctor_appointments = document.getElementById('show-doctor-appointments')
var all_doctor_appointments = document.getElementById('show-all-doctors-appointments')

function hideShowThisDoctor() {
    this_doctor_appointments.style.display = 'block';
    all_doctor_appointments.style.display = 'none';
}

function hideShowAllDoctors() {
    this_doctor_appointments.style.display = 'none';
    all_doctor_appointments.style.display = 'block';
}

function ConfirmLogout() {
    var result = confirm('Are you sure you want to log out?')
    if (result == false) {
        event.preventDefault();
    }
}

function confirm_cancel_or_reschedule_appointment() {
    var result = confirm('Are you sure?');
    if (result == false) {
        event.preventDefault();
    }
}