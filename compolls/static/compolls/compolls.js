console.log("Hello")

document.getElementById("button-a").addEventListener('click', () => {
    console.log("you clicked A");

    const user_data = {
        choice: 'A'
    };

    // fetch('ajax/manage_vote')
    // .then(response => response.json())
    // .then(data => console.log(data))

    fetch('ajax/manage_vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(user_data),
    })
    // .then(response => response.json())
    // .then(data => console.log(data))

})
