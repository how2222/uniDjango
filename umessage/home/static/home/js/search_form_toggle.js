document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.getElementById('searchButton');
    const searchFormSection = document.getElementById('searchFormSection');
    const submitButton = document.getElementById('submitButton');
    
    if (searchButton && searchFormSection) {
        searchButton.addEventListener('click', function(e) {
            e.preventDefault();
            
            searchFormSection.classList.toggle('hidden');
            
            setTimeout(() => {
                searchFormSection.classList.toggle('opacity-0');
            }, 10);
            
            if (!searchFormSection.classList.contains('hidden')) {
                const symbolInput = document.getElementById('symbol');
                if (symbolInput) {
                    symbolInput.focus();
                }
                searchFormSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
});