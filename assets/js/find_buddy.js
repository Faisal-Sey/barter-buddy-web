
async function ViewModal(id) {
  url = "http://localhost:8000/get-profile"
  data = {id:id}
  await fetch(url, {
    method: "POST",
    mode: "same-origin",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json"
    }
  }).then((resp) => resp.json())
  .then((data) => {
    const profile = data?.profile
    console.log(profile)
    document.getElementById("fname").innerText = profile.fname;
    document.getElementById("lname").innerText = profile.lname;
    document.getElementById("age").innerText = profile.age;
    document.getElementById("location").innerText = profile.location;
    document.getElementById("skills").innerText = profile.skills;
    document.getElementById("about").innerText = profile.about;
    document.getElementById("email").innerText = profile.email;

  })

  // var body = "Welcome to ASPSnippets.com";
  // $("#viewModal .modal-body").html(body);
  $("#viewModal").modal("show");
}


const capitalizeFirstLetter = (name) => {
  const nameTrimmed = name.trim()
  const firstLetter = nameTrimmed[0].toUpperCase()
  return firstLetter + nameTrimmed.slice(1)
}

async function ConnectModal(id, user_id) {
  url = "http://localhost:8000/get-profile"
  data = {id:id}
  await fetch(url, {
    method: "POST",
    mode: "same-origin",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json"
    }
  }).then((resp) => resp.json())
  .then((data) => {
    const profile = data?.profile
    profile?.skills_arr?.forEach(elt => {
      const opt = document.createElement("option")
      opt.setAttribute("value", elt)
      console.log(capitalizeFirstLetter(elt))
      opt.innerText = capitalizeFirstLetter(elt)

      const skillSelect = document.getElementById("skills_select")
      skillSelect.appendChild(opt)
    });

    document.getElementById("receiver_id").value = user_id;

  })

  // var body = "Welcome to ASPSnippets.com";
  // $("#viewModal .modal-body").html(body);
  $("#connectModal").modal("show");
}

async function CreateConnectModal(id) {
  url = "http://localhost:8000/get-profile"
  data = {id:id}
  await fetch(url, {
    method: "POST",
    mode: "same-origin",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json"
    }
  }).then((resp) => resp.json())
  .then((data) => {
    const profile = data?.profile
    profile?.skills_arr?.forEach(elt => {
      const opt = document.createElement("option")
      opt.setAttribute("value", elt)
      console.log(capitalizeFirstLetter(elt))
      opt.innerText = capitalizeFirstLetter(elt)

      const skillSelect = document.getElementById("skills_select")
      skillSelect.appendChild(opt)
    });


  })

  // var body = "Welcome to ASPSnippets.com";
  // $("#viewModal .modal-body").html(body);
  $("#connectModal").modal("show");
}