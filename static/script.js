document.addEventListener("DOMContentLoaded", () => {
  const gender = localStorage.getItem("friendGender", "boyfriend");
  const friendTitle = document.getElementById("friend-title");
  const avatarImg = document.getElementById("avatarImg");
  const speakingGif = document.getElementById("speakingGif");
  const btn = document.getElementById("speakBtn");
  const audioElem = document.getElementById("audio");
  const replyText = document.getElementById("replyText");

  if (gender && friendTitle && avatarImg) {
    const titles = {
      male: "🧑 Talking to Your Brotherly Friend",
      female: "👩 Talking to Your Sisterly Friend",
      boyfriend: "💘 Talking to Your Boyfriend",
      girlfriend: "💖 Talking to Your Girlfriend"
    };
    friendTitle.innerText = titles[gender] || titles.male;

    const avatars = {
      male: "/static/avatars/boy.png",
      female: "/static/avatars/girl.png",
      boyfriend: "/static/avatars/boy.png",
      girlfriend: "/static/avatars/girl.png"
    };
    avatarImg.src = avatars[gender] || avatars.male;
  }

  audioElem.onplay = () => {
    speakingGif.style.display = "block";
  };

  audioElem.onended = () => {
    speakingGif.style.display = "none";
  };

  btn.addEventListener("click", async () => {
    const message = document.getElementById("inputText").value.trim();

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
