function setupSidebarNavigation() {
  const navItems = document.querySelectorAll(".nav-item")

  const currentUrl = window.location.pathname

  navItems.forEach((item) => {
    const link = item.querySelector("a")
    if (link.getAttribute("href") === currentUrl) {
      item.classList.add("active")
    } else {
      item.classList.remove("active")
    }
  })
}

document.addEventListener("DOMContentLoaded", setupSidebarNavigation)


function toggleDropdown() {
    const dropdown = document.getElementById("profileDropdown");
    dropdown.style.display = (dropdown.style.display === "block") ? "none" : "block";
}

document.addEventListener('click', function(event) {
    const dropdown = document.getElementById("profileDropdown");
    const profile = document.querySelector('.user-profile');
    if (!profile.contains(event.target)) {
        dropdown.style.display = 'none';
    }
});