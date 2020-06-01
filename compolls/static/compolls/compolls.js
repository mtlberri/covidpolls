console.log("Hello");

var user = 'Hotman'

function ajax_vote(id)  {

    console.log(`you clicked ${id}`);

    var csrftoken = Cookies.get('csrftoken');

    const user_vote_data = {
        user: user,
        choice_id: id,
    };

    console.log(JSON.stringify(user_vote_data));

    // fetch('ajax/manage_vote')
    // .then(response => response.json())
    // .then(data => console.log(data))

    fetch('ajax/manage_vote', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(user_vote_data),
    })
    .then(response => response.json())
    .then(data => console.log(data));

};

