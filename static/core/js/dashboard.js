const replies = [
  "Dekoratorlar funksional dasturlashning asosiy qismi! Batafsil misol ko'rsatayinmi?",
  "Zo'r savol! Bu mavzu Python'da keng qo'llaniladi.",
  "Albatta tushuntiraman. Qaysi qismidan boshlaymiz?",
  "Bu konsept dastlab qiyin ko'rinadi, lekin amaliy misollar bilan tushunib ketasiz.",
  "Aniq tushuntirishim uchun qaysi kurs doirasida so'rayapsiz?",
];
let ri = 0;

function sendMsg() {
  const inp = document.getElementById("chat-in");
  const msgs = document.getElementById("chat-msgs");
  const txt = inp.value.trim();
  if (!txt) return;

  const userMsg = document.createElement("div");
  userMsg.className = "chat-msg msg-user";
  userMsg.textContent = txt;
  msgs.appendChild(userMsg);
  inp.value = "";
  msgs.scrollTop = msgs.scrollHeight;

  // Typing indicator
  const typing = document.createElement("div");
  typing.className = "msg-ai";
  typing.style.cssText =
    "display:flex;gap:4px;padding:10px 14px;border-radius:12px 12px 12px 3px;border:1px solid var(--border);width:fit-content;";
  typing.innerHTML =
    '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
  msgs.appendChild(typing);
  msgs.scrollTop = msgs.scrollHeight;

  setTimeout(() => {
    typing.remove();
    const aiMsg = document.createElement("div");
    aiMsg.className = "chat-msg msg-ai";
    aiMsg.textContent = replies[ri % replies.length];
    ri++;
    msgs.appendChild(aiMsg);
    msgs.scrollTop = msgs.scrollHeight;
  }, 1200);
}
