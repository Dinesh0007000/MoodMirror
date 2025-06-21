document.addEventListener("DOMContentLoaded", () => {
  const gender = localStorage.getItem("friendGender");
  const friendTitle = document.getElementById("friend-title");
  const avatarImg = document.getElementById("avatarImg");
  const speakingGif = document.getElementById("speakingGif");
  const btn = document.getElementById("speakBtn");
  const audioElem = document.getElementById("audio");
  const replyText = document.getElementById("replyText");

  // Set avatar and title
  if (gender && friendTitle && avatarImg) {
    friendTitle.innerText =
      gender === "male"
        ? "🧑 Talking to Your Brotherly Friend"
        : "👩 Talking to Your Sisterly Friend";

    avatarImg.src =
      gender === "male"
        ? "/static/avatars/boy.png"
        : "/static/avatars/girl.png";
  }

  // Audio play & end handlers for showing/hiding GIF
  audioElem.onplay = () => {
    speakingGif.style.display = "block";
  };

  audioElem.onended = () => {
    speakingGif.style.display = "none";
  };

  btn.addEventListener("click", async () => {
    const message = document.getElementById("inputText").value.trim();

    // Reset response
    replyText.innerText = "Thinking... 🧠";
    speakingGif.style.display = "none";
    audioElem.style.display = "none";

    if (!message) {
      replyText.innerText = "Please share something, I'm listening 💬";
      return;
    }

    try {
      const response = await fetch("/talk", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, gender }),
      });

      const data = await response.json();
      replyText.innerText = data.reply;

      if (data.audio) {
        audioElem.src = data.audio;
        audioElem.style.display = "block";
        audioElem.play();
      }
    } catch (err) {
      replyText.innerText = "Oops! Something went wrong. 😓";
      console.error("Error talking:", err);
    }
  });
});
