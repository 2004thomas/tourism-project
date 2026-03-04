// 1. Dark Mode Toggle
// const toggleBtn = document.getElementById('theme-toggle');
// toggleBtn.addEventListener('click', () => {
//     const currentTheme = document.body.getAttribute('data-theme');
//     if (currentTheme === 'dark') {
//         document.body.removeAttribute('data-theme');
//     } else {
//         document.body.setAttribute('data-theme', 'dark');
//     }
// });



  const toggleBtn = document.getElementById("themeToggle");
  const htmlTag = document.documentElement;

  // Load saved theme
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




// 2. Filter Logic
// const filterButtons = document.querySelectorAll('.filter-btn');
// const cards = document.querySelectorAll('.card');

// filterButtons.forEach(button => {
//     button.addEventListener('click', () => {
//         // Remove active class from all buttons
//         filterButtons.forEach(btn => btn.classList.remove('active'));
//         button.classList.add('active');

//         const filterValue = button.getAttribute('data-filter');

//         cards.forEach(card => {
//             if (filterValue === 'all' || card.classList.contains(filterValue)) {
//                 card.classList.remove('hide');
//             } else {
//                 card.classList.add('hide');
//             }
//         });
//     });
// });



  const filterButtons = document.querySelectorAll(".filter-btn");
  const cards = document.querySelectorAll(".place-card");

  filterButtons.forEach(button => {
    button.addEventListener("click", () => {

      // Remove active state
      filterButtons.forEach(btn => btn.classList.remove("active"));
      button.classList.add("active");

      const filterValue = button.getAttribute("data-filter");

      cards.forEach(card => {
        if (filterValue === "all") {
          card.classList.remove("d-none");
        } else {
          if (card.classList.contains(filterValue)) {
            card.classList.remove("d-none");
          } else {
            card.classList.add("d-none");
          }
        }
      });

    });
  });

//

// const toggleBtnFilter = document.getElementById("filterToggle");
// const options = document.getElementById("filterOptions");

// toggleBtn.addEventListener("click", function() {
//   options.classList.toggle("show");
// });


// 

function filterPlaces(category){
  const cards=document.querySelectorAll(".place-card");
  cards.forEach(card=>{
    if(category==="all"){
      card.style.display="block";
    }
    else if(card.classList.contains(category)){
      card.style.display="block";
    }
    else{
      card.style.display="none";
    }
  });
}

filterButtons.forEach(button => {
  button.addEventListener("click", function() {

    filterButtons.forEach(btn => btn.classList.remove("active"));
    this.classList.add("active");

    const filterValue = this.getAttribute("data-filter");

    document.querySelectorAll(".place-card").forEach(card => {
      if (filterValue === "all") {
        card.classList.remove("d-none");
      } else {
        card.classList.toggle("d-none", !card.classList.contains(filterValue));
      }
    });

  });
});


