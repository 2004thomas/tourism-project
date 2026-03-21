
  const toggleBtn = document.getElementById("themeToggle");
  const htmlTag = document.documentElement;

  // // Load saved theme
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme) {
    htmlTag.setAttribute("data-bs-theme", savedTheme);
    updateIcon(savedTheme);
  }

  toggleBtn.addEventListener("click", () => {
    const currentTheme = htmlTag.getAttribute("data-bs-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";

    htmlTag.setAttribute("data-bs-theme", newTheme);
    localStorage.setItem("theme", newTheme);
    updateIcon(newTheme);
  });

  function updateIcon(theme) {
    toggleBtn.innerHTML =
      theme === "dark"
        ? '<i class="bi bi-moon-fill"></i>'
        : '<i class="bi bi-sun-fill"></i>';
  }

//   const filterButtons = document.querySelectorAll(".filter-btn");
//   const cards = document.querySelectorAll(".place-card");

//   filterButtons.forEach(button => {
//     button.addEventListener("click", () => {

//       // Remove active state
//       filterButtons.forEach(btn => btn.classList.remove("active"));
//       button.classList.add("active");

//       const filterValue = button.getAttribute("data-filter");

//       cards.forEach(card => {
//         if (filterValue === "all") {
//           card.classList.remove("d-none");
//         } else {
//           if (card.classList.contains(filterValue)) {
//             card.classList.remove("d-none");
//           } else {
//             card.classList.add("d-none");
//           }
//         }
//       });

//     });
//   });

// function filterPlaces(category){
//   const cards=document.querySelectorAll(".place-card");
//   cards.forEach(card=>{
//     if(category==="all"){
//       card.style.display="block";
//     }
//     else if(card.classList.contains(category)){
//       card.style.display="block";
//     }
//     else{
//       card.style.display="none";
//     }
//   });
// }

// filterButtons.forEach(button => {
//   button.addEventListener("click", function() {

//     filterButtons.forEach(btn => btn.classList.remove("active"));
//     this.classList.add("active");

//     const filterValue = this.getAttribute("data-filter");

//     document.querySelectorAll(".place-card").forEach(card => {
//       if (filterValue === "all") {
//         card.classList.remove("d-none");
//       } else {
//         card.classList.toggle("d-none", !card.classList.contains(filterValue));
//       }
//     });

//   });
// });


// THEME LOAD (runs on every page)
// document.addEventListener("DOMContentLoaded", function () {

//     const savedTheme = localStorage.getItem("theme");

//     if (savedTheme === "dark") {
//         document.body.classList.add("dark-mode");
//     }

// });


// // THEME TOGGLE
// const toggleBtn = document.getElementById("themeToggle");

// if (toggleBtn) {
//     toggleBtn.addEventListener("click", () => {

//         document.body.classList.toggle("dark-mode");

//         localStorage.setItem(
//             "theme",
//             document.body.classList.contains("dark-mode") ? "dark" : "light"
//         );

//     });
// }


// // FILTER (only runs if elements exist)
// const filterButtons = document.querySelectorAll(".filter-btn");
// const cards = document.querySelectorAll(".place-card");

// if (filterButtons.length > 0) {

//     filterButtons.forEach(button => {

//         button.addEventListener("click", () => {

//             filterButtons.forEach(btn => btn.classList.remove("active"));
//             button.classList.add("active");

//             const filterValue = button.getAttribute("data-filter");

//             cards.forEach(card => {

//                 const category = card.getAttribute("data-category");

//                 if (filterValue === "all" || category === filterValue) {
//                     card.style.display = "block";
//                 } else {
//                     card.style.display = "none";
//                 }

//             });

//         });

//     });

// }