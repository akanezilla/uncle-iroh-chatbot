const sendButton = document.getElementById('sendButton');
const userInput = document.getElementById('userInput');
const chatBox = document.getElementById('chatBox');

sendButton.addEventListener('click', () => {
  const message = userInput.value.trim(); 

  if (message) {
    const userMessage = document.createElement('p'); 
    userMessage.textContent = message; 
    userMessage.classList.add('user-message'); 

    chatBox.appendChild(userMessage);
    userInput.value = ''; 
    chatBox.scrollTop = chatBox.scrollHeight;
  }
});
