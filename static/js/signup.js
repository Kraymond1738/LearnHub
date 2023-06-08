//create a json to send to backend
const signupForm = document.getElementById('signupForm');

signupForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(signupForm);

  // Convert the form data to an object
  const data = {};
  for (let [key, value] of formData.entries()) {
    data[key] = value;
  }
  console.log(data)

  // Send the data to the backend using fetch
  fetch('/signup', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(result => {
    console.log(result);
  })
  .catch(error => {
    console.error('Error:', error);
  });
});
