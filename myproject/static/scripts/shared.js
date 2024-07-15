let chatbotOverlayElement = document.getElementById("chatbot-overlay");
let questionChatbotElement = document.getElementById("question-chatbot");

function displayChatbotOverlay() {
  if (chatbotOverlayElement.style.display == "block") {
    chatbotOverlayElement.style.display = "none";
  } else {
    chatbotOverlayElement.style.display = "block";
  }
}

questionChatbotElement.addEventListener("click", displayChatbotOverlay);
