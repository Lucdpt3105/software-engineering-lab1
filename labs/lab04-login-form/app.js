const f = document.getElementById("loginForm");
const u = document.getElementById("username");
const p = document.getElementById("password");
const msg = document.getElementById("msg");
document.getElementById("cancelBtn").onclick = () => { u.value=""; p.value=""; msg.textContent=""; };

f.addEventListener("submit", (e) => {
  e.preventDefault();
  msg.textContent = "";
  if (!u.value.trim() || !p.value.trim()) {
    msg.textContent = "Vui lòng nhập Username/Password.";
    return;
  }
  if (p.value.length < 4) {
    msg.textContent = "Password tối thiểu 4 ký tự.";
    return;
  }
  // Demo: giả lập login ok/sai
  const ok = u.value === "demo" && p.value === "1234";
  msg.style.color = ok ? "#86efac" : "#fca5a5";
  msg.textContent = ok ? "Login thành công!" : "Sai thông tin đăng nhập.";
});
