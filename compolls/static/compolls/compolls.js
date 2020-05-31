console.log("Hello");

document.getElementById("button-choice-a").addEventListener('click', () => {
    console.log("you clicked A");
    console.log(event.target.id);

    var csrftoken = Cookies.get('csrftoken');

    const user_data = {
        choice: 'A',
    };

    console.log(JSON.stringify(user_data));

    // fetch('ajax/manage_vote')
    // .then(response => response.json())
    // .then(data => console.log(data))

    fetch('ajax/manage_vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(user_data),
    })
    .then(response => response.json())
    .then(data => console.log(data));

});
