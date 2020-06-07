console.log("Hello");

var user = '';

function ajax_vote(id)  {

    console.log(`you clicked ${id}`);
    
    if (user != '') {
        var csrftoken = Cookies.get('csrftoken');

        const user_vote_data = {
            user: user,
            choice_id: id,
        };

        console.log('user vote being sent to server:')
        console.log(JSON.stringify(user_vote_data));

        fetch('ajax/manage_vote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(user_vote_data),
        })
        .then(response => response.json())
        .then(data => {
            console.log('data being received back from server:');
            console.log(data);

            // Fill the list of voters A
            var ul = document.getElementById("list_choice_a");
            var voters_a_length = data.voters.voters_for_a.length;
            for (var i = 0; i < voters_a_length; i++) {
                var li = document.createElement("li");
                li.appendChild(document.createTextNode(data.voters.voters_for_a[i]));
                ul.appendChild(li);
            }
            // Fill the list of voters B
            var ul = document.getElementById("list_choice_b");
            var voters_b_length = data.voters.voters_for_b.length;
            for (var i = 0; i < voters_b_length; i++) {
                var li = document.createElement("li");
                li.appendChild(document.createTextNode(data.voters.voters_for_b[i]));
                ul.appendChild(li);
            }

            // Change the button style after vote completed
            document.getElementById(id).className = "btn btn-success";
            document.getElementById(id).innerText = "Voted";
        });
    } else {
        console.log('cannot vote if username empty')
    }

};

document.getElementById("btn-save-name").addEventListener('click', (e) => {

    console.log('you clicked save name');
    input_value = document.getElementById("name-input").value;

    if (input_value != "") {
        user = document.getElementById("name-input").value;
        console.log("user name: " + user);
        
        document.getElementById("btn-save-name").className = "btn btn-success";
        document.getElementById("btn-save-name").innerText = "Saved";

        document.getElementById("chosen-name").innerHTML = "You will vote under the name: " +
        "<span class='badge badge-pill badge-success'>" + user + "</span>";
    } else {
        console.log('user name is empty')
    }

});

