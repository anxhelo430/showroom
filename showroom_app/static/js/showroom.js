const contactForm = document.getElementById("contactForm");
const successMessage = document.getElementById("successMessage");

if (contactForm) {
  contactForm.addEventListener("submit", function (event) {
    event.preventDefault();

    contactForm.classList.add("was-validated");

    if (contactForm.checkValidity()) {
      successMessage.classList.remove("d-none");

      contactForm.reset();
      contactForm.classList.remove("was-validated");
    }
  });
}

const filterButtons = document.querySelectorAll(".filter-btn");
const modelItems = document.querySelectorAll(".model-item");

filterButtons.forEach(function (button) {
  button.addEventListener("click", function () {
    const selectedCategory = button.dataset.filter;

    filterButtons.forEach(function (filterButton) {
      filterButton.classList.remove("active");
    });

    button.classList.add("active");

    modelItems.forEach(function (model) {
      if (
        selectedCategory === "all" ||
        model.dataset.category === selectedCategory
      ) {
        model.classList.remove("d-none");
      } else {
        model.classList.add("d-none");
      }
    });
  });
});



const newsletterForm = document.getElementById("newsletterForm");
const newsletterSuccess = document.getElementById("newsletterSuccess");

if (newsletterForm) {
  newsletterForm.addEventListener("submit", function (event) {
    event.preventDefault();

    newsletterForm.classList.add("was-validated");

    if (newsletterForm.checkValidity()) {
      newsletterSuccess.classList.remove("d-none");

      newsletterForm.reset();
      newsletterForm.classList.remove("was-validated");
    }
  });
}
const siteSearchForm = document.getElementById("siteSearchForm");
const siteSearchInput = document.getElementById("siteSearchInput");

if (siteSearchForm) {
  siteSearchForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const searchTerm = siteSearchInput.value.trim();

    if (searchTerm) {
      window.location.href =
        "models.html?search=" + encodeURIComponent(searchTerm);
    }
  });
}
const searchParameters = new URLSearchParams(window.location.search);
const modelSearchTerm = searchParameters.get("search");

if (modelSearchTerm && modelItems.length > 0) {
  const normalizedSearchTerm = modelSearchTerm.toLowerCase();

  filterButtons.forEach(function (button) {
    button.classList.remove("active");
  });

  modelItems.forEach(function (model) {
    const carInformation = model.textContent.toLowerCase();

    if (carInformation.includes(normalizedSearchTerm)) {
      model.classList.remove("d-none");
    } else {
      model.classList.add("d-none");
    }
  });
}