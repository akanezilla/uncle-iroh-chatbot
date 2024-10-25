const inputField = document.querySelector('input');
const button = document.querySelector('button');

button.addEventListener('click', () => {
  const userInput = inputField.value.trim();
  if (userInput) {
    alert(`You said: "${userInput}". Uncle Iroh is pleased.`);
    inputField.value = ''; // Clear input after sending
  }
});
