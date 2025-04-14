const dateInput = document.getElementById('id_start_date'); // Select the date input by ID

// Create a date picker instance
const picker = MCDatepicker.create({
    el: '#id_start_date',
    dateFormat: 'yyyy-mm-dd', // Set the desired date format
    closeOnBlur: true, // Close picker when clicking outside
    selectedDate: new Date(), // Default to today's date
    theme: {
        theme_color: '#6c584c'
    }
});

// Open the date picker when the input is clicked
dateInput.addEventListener("click", () => {
    picker.open();
});
