function formatDate(dateString) {
    const inputDate = new Date(dateString);
    const options = {
        day: 'numeric',
        month: 'short',
        year: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    };
    const formattedDate = inputDate.toLocaleDateString('en-au', options);
    return formattedDate;
}

window.addEventListener('DOMContentLoaded', (event) => {
    const dateElements = document.getElementsByClassName('date-time');
    for (let i = 0; i < dateElements.length; i++) {
        const dateElement = dateElements[i];
        const dateString = dateElement.innerHTML;
        const formattedDate = formatDate(dateString);
        dateElement.innerHTML = formattedDate;
    }
});
