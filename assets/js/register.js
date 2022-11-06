const form = document.querySelector(".sign-up__form");
const inputs = document.querySelectorAll(".form__input");
/*
clearInputs(inputs);
form.addEventListener("submit", (e) => {
  e.preventDefault();
  inputs.forEach((input) => {
    let inputValue = input.firstElementChild;
    if (inputValue.getAttribute("id") === "email") {
      validateEmail(inputValue, input);
    } else {
      validateLength(inputValue, input);
    }
  });
});*/

function clearInputs() {
  inputs.forEach((input) => {
    let inputValue = input.firstElementChild;
    inputValue.value = "";
  });
}

function validateEmail(email, parent) {
  const validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if (!email.value.match(validRegex)) {
    parent.classList.add("warning");
    email.style.color = "var(--Red)";
  } else {
    parent.classList.remove("warning");
    email.style.color = "var(--Dark-Blue)";
  }
}

function validateLength(string, parent) {
  if (!string.value.length > 0) {
    parent.classList.add("warning");
    string.style.color = "var(--Red)";
  } else {
    parent.classList.remove("warning");
    string.style.color = "var(--Dark-Blue)";
  }
}

async function registerUser() {
  const password = document.getElementById("password").value;
  const cPassword = document.getElementById("c_password").value;
  const fname = document.getElementById("fname").value;
  const lname = document.getElementById("lname").value;
  const email = document.getElementById("email").value;
  const username = document.getElementById("username").value;

  if (password === cPassword) {
    const url = "https://localhost:8000/login"
    const data = {
      password: password,
      fname: fname,
      lname: lname,
      email: email,
      username: username
    }
    await fetch(url, {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json"
      }
    }).then(resp => {
      console.log(JSON.stringify(resp.json()))
    })
  }
}
