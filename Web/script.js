document.addEventListener("DOMContentLoaded", function() {
    const greeting = document.createElement("p");
    const currentHour = new Date().getHours();
    
    if (currentHour < 12) {
        greeting.textContent = "Good morning! Start your day with learning.";
    } else if (currentHour < 18) {
        greeting.textContent = "Good afternoon! Keep up the learning momentum.";
    } else {
        greeting.textContent = "Good evening! It's never too late to learn something new.";
    }

    document.getElementById("home").appendChild(greeting);
});
