function switchTab(tab) {
  document
    .querySelectorAll(".tab-btn")
    .forEach((b, i) =>
      b.classList.toggle(
        "active",
        (i === 0 && tab === "login") || (i === 1 && tab === "register"),
      ),
    );
  document
    .getElementById("panel-login")
    .classList.toggle("active", tab === "login");
  document
    .getElementById("panel-register")
    .classList.toggle("active", tab === "register");
  document.getElementById("success-screen").style.display = "none";
}

function togglePw(id, btn) {
  const inp = document.getElementById(id);
  const isText = inp.type === "text";
  inp.type = isText ? "password" : "text";
  btn.querySelector(".eye-icon").style.opacity = isText ? "1" : ".4";
}

function checkStrength(val) {
  const el = document.getElementById("pw-strength");
  const label = document.getElementById("pw-label");
  const bars = [
    document.getElementById("bar1"),
    document.getElementById("bar2"),
    document.getElementById("bar3"),
    document.getElementById("bar4"),
  ];
  if (!val) {
    el.style.display = "none";
    return;
  }
  el.style.display = "block";
  let score = 0;
  if (val.length >= 8) score++;
  if (/[A-Z]/.test(val)) score++;
  if (/[0-9]/.test(val)) score++;
  if (/[^A-Za-z0-9]/.test(val)) score++;
  const cls = score <= 1 ? "weak" : score <= 2 ? "medium" : "strong";
  const labels = ["", "Zaif", "O'rtacha", "Yaxshi", "Kuchli"];
  bars.forEach((b, i) => {
    b.className = "pw-bar";
    if (i < score) b.classList.add(cls);
  });
  label.textContent = labels[score] || "";
  label.style.color =
    cls === "weak" ? "#EF4444" : cls === "medium" ? "#F59E0B" : "#10B981";
}

function handleLogin(e) {
  e.preventDefault();
  const btn = e.target.querySelector(".submit-btn");
  btn.textContent = "Tekshirilmoqda...";
  btn.disabled = true;
  setTimeout(() => {
    document.getElementById("panel-login").classList.remove("active");
    document.getElementById("success-screen").style.display = "block";
  }, 1200);
}

function handleRegister(e) {
  e.preventDefault();
  const btn = e.target.querySelector(".submit-btn");
  btn.innerHTML = "Yaratilmoqda...";
  btn.disabled = true;
  setTimeout(() => {
    document.getElementById("panel-register").classList.remove("active");
    document.getElementById("success-screen").style.display = "block";
  }, 1400);
}
