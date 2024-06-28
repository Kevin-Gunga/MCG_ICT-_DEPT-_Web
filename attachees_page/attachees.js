const attendanceButtonElement = document.getElementById('attendance-button');
const cancelAttendanceButtonElement = document.getElementById('remove-attendance-form');

const attendanceFormElement = document.getElementById('form-2');
const backdropElement = document.getElementById('backdrop');

function displayAttendanceOverlay () {
    attendanceFormElement.style.display = 'block';
    backdropElement.style.display = 'block';
}

attendanceButtonElement.addEventListener('click', displayAttendanceOverlay);

function removeAttendanceForm() {
    attendanceFormElement.style.display = 'none';
    backdropElement.style.display = 'none';
}

cancelAttendanceButtonElement.addEventListener('click',removeAttendanceForm);
backdropElement.addEventListener('click',removeAttendanceForm)