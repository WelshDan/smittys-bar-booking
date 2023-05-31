/* ..... Dropdown Menu ..... */
function linkToPage() {
   const dropdown = document.getElementById("dropdown");
   const chosenOption = dropdown.value;
   if (chosenOption !== "") {
    window.location.href = chosenOption;
   }
}