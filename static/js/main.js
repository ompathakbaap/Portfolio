// Init AOS
AOS.init({ duration: 650, once: true, offset: 70 });

// Tilt cards (stat cards)
try {
  VanillaTilt.init(document.querySelectorAll("[data-tilt]"), { max: 10, speed: 700, glare: true, "max-glare": 0.18 });
} catch (e) {}

// Year in footer
document.getElementById("year").textContent = new Date().getFullYear();

// Scroll progress bar
const progress = document.getElementById("progress");
window.addEventListener("scroll", () => {
  const h = document.documentElement;
  const scrolled = (h.scrollTop) / (h.scrollHeight - h.clientHeight);
  progress.style.width = `${Math.min(1, Math.max(0, scrolled)) * 100}%`;
});

// Theme toggle (dark only by default, but this gives a "slate" light mode)
const themeToggle = document.getElementById("themeToggle");
const sun = document.getElementById("sun");
const moon = document.getElementById("moon");
const html = document.documentElement;

function setTheme(mode) {
  if (mode === "light") {
    html.classList.add("light");
    document.body.classList.remove("bg-slate-950");
    document.body.classList.add("bg-slate-50", "text-slate-950");
    moon.classList.add("hidden");
    sun.classList.remove("hidden");
  } else {
    html.classList.remove("light");
    document.body.classList.remove("bg-slate-50", "text-slate-950");
    document.body.classList.add("bg-slate-950", "text-slate-100");
    sun.classList.add("hidden");
    moon.classList.remove("hidden");
  }
  localStorage.setItem("theme", mode);
}

const saved = localStorage.getItem("theme");
if (saved) setTheme(saved);

themeToggle?.addEventListener("click", () => {
  const isLight = html.classList.contains("light");
  setTheme(isLight ? "dark" : "light");
});

// GSAP hero animation
gsap.registerPlugin(ScrollTrigger);

gsap.from("h1", { y: 18, opacity: 0, duration: 0.8, ease: "power2.out" });
gsap.from(".btn-primary, .btn-secondary, .btn-ghost", { y: 10, opacity: 0, duration: 0.7, ease: "power2.out", stagger: 0.08, delay: 0.15 });
gsap.from(".statcard", { y: 10, opacity: 0, duration: 0.7, ease: "power2.out", stagger: 0.08, delay: 0.25 });

// Count-up animation for highlight numbers
function animateCount(el) {
  const raw = (el.textContent || "").trim();
  // Extract numeric part (supports % and + and "yr")
  const m = raw.match(/([\d.]+)/);
  if (!m) return;
  const end = parseFloat(m[1]);
  const suffix = raw.replace(m[1], "");
  const obj = { val: 0 };
  gsap.to(obj, {
    val: end,
    duration: 1.0,
    ease: "power2.out",
    onUpdate: () => {
      const v = end >= 10 ? Math.round(obj.val) : Math.round(obj.val * 10) / 10;
      el.textContent = `${v}${suffix}`;
    }
  });
}

ScrollTrigger.batch(".statnum", {
  start: "top 85%",
  once: true,
  onEnter: (batch) => batch.forEach(animateCount)
});

// Contact form -> mailto
window.openMailto = function openMailto(ev) {
  ev.preventDefault();
  const name = document.getElementById("c_name").value.trim();
  const email = document.getElementById("c_email").value.trim();
  const subject = document.getElementById("c_subject").value.trim();
  const message = document.getElementById("c_message").value.trim();

  const body = encodeURIComponent(
`Hi Om,

${message}

— ${name}
${email}`
  );

  const mail = "EMAIL"; // placeholder replaced server-side? keep as is and use data-email attribute?
  // We'll pull from DOM (from the mailto link)
  const target = document.querySelector('a[href^="mailto:"]');
  const to = target ? target.getAttribute("href").replace("mailto:", "") : "ompathak61@gmail.com";

  window.location.href = `mailto:${to}?subject=${encodeURIComponent(subject)}&body=${body}`;
  return false;
};
