function openInvestPopup(projectTitle) {

    document.getElementById('invest-popup').style.display = 'flex';
    
    document.getElementById('project-title').innerText = 'Invest in ' + projectTitle;
}

function closeInvestPopup() {
    
    document.getElementById('invest-popup').style.display = 'none';
}

// function sendInvestment() {
    
//     const amount = document.getElementById('invest-amount').value;
//     if (amount) {
//         alert(`Investment of ${amount} sent successfully!`);
       
//         closeInvestPopup();
//     } else {
//         alert('Please enter a valid amount.');
//     }
// }
